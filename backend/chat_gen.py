from typing import *
from autogen import *
from autogen import Agent
from autogen import ConversableAgent
import sys
import os
from pathlib import Path
from autogen.coding import CodeBlock, LocalCommandLineCodeExecutor
import prompts
import tempfile

# Consts
INIT_AGENT_NAME = 'init_agent'
TEXTBOOK_AGENT_NAME = 'textbook_agent'
MANIM_CODING_AGENT_NAME = 'manim_coding_agent'
MANIM_CODING_REVIEW_AGENT_NAME = 'manim_coding_review_agent'
CODE_EXEC_AGENT_NAME = 'code_exec_agent'
CODE_EXEC_INSTRUCT_AGENT_NAME = 'code_exec_instruct_agent'


agents = {}


def state_transition(
    last_speaker: Agent, 
    groupchat: GroupChat                    
) -> Union[Agent, Literal['auto', 'manual', 'random' 'round_robin'], None]:
    messages = groupchat.messages

    
    if last_speaker is agents[INIT_AGENT_NAME]:
        return agents[TEXTBOOK_AGENT_NAME]
    elif last_speaker is agents[TEXTBOOK_AGENT_NAME]:
        return agents[MANIM_CODING_AGENT_NAME]
    elif last_speaker is agents[MANIM_CODING_AGENT_NAME]:
        return agents[MANIM_CODING_REVIEW_AGENT_NAME]
    elif last_speaker is agents[MANIM_CODING_REVIEW_AGENT_NAME]:
        if "REVIEW DONE" in messages[-1]["content"]:
            return agents[CODE_EXEC_INSTRUCT_AGENT_NAME]
        else:
            return agents[MANIM_CODING_AGENT_NAME]
    elif last_speaker is agents[CODE_EXEC_INSTRUCT_AGENT_NAME]:
        return agents[CODE_EXEC_AGENT_NAME]
    elif last_speaker is agents[CODE_EXEC_AGENT_NAME]:
        # Logic to go back to coding step if execution fails for some reason
        # Will probably need a max_retries so it doesnt run infinitely
        # if messages[-1]["content"] == "exitcode: 1":
        #     # runs code -> execution failed --> go back to code generation agent
        #     return agents[MANIM_CODING_AGENT_NAME]
        # else:
        #     # runs code -> execution success -> DONE
        return None


def main(user_query: str):
    # example LLM config for the entrypoint agent
    llm_config = {
        "config_list": [
            {"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}
        ]
    }
    
    # Claude - only uses claude if the claude api key is set in env
    claude_api_key = os.environ.get("CLAUDE_API_KEY")
    claude_llm_config = None
    if claude_api_key is None:
        claude_llm_config = llm_config
    else:
        claude_llm_config = {
            "config_list": [
                {
                    "model": "claude-3-5-sonnet-20241022",
                    "api_key": claude_api_key,
                    "api_type": "anthropic",
                }
            ]
        }
    
    # the initializer agent
    init_agent_system_message = prompts.get_init_agent_prompt()
    init_agent = ConversableAgent(
        INIT_AGENT_NAME,
        system_message=init_agent_system_message,
        llm_config=llm_config,
    )
    agents[INIT_AGENT_NAME] = init_agent
    
    textbook_agent_prompt = prompts.get_textbook_agent_prompt()
    textbook_agent = ConversableAgent(
        TEXTBOOK_AGENT_NAME,
        system_message=textbook_agent_prompt,
        llm_config=llm_config,
        max_consecutive_auto_reply=1,
        human_input_mode="NEVER",
    )
    agents[TEXTBOOK_AGENT_NAME] = textbook_agent

    manim_coding_agent_prompt = prompts.get_manim_coding_agent_prompt()
    manim_coding_agent = ConversableAgent(
        MANIM_CODING_AGENT_NAME,
        system_message=manim_coding_agent_prompt,
        llm_config=claude_llm_config,
        code_execution_config=False,
        max_consecutive_auto_reply=3,
        human_input_mode="NEVER",
    )
    agents[MANIM_CODING_AGENT_NAME] = manim_coding_agent
    
    manim_coding_review_agent_prompt = prompts.get_manim_coding_review_agent_prompt()
    manim_coding_review_agent = ConversableAgent(
        MANIM_CODING_REVIEW_AGENT_NAME,
        system_message=manim_coding_review_agent_prompt,
        llm_config=claude_llm_config,
        code_execution_config=False,
        max_consecutive_auto_reply=3,
        human_input_mode="NEVER",
    )
    agents[MANIM_CODING_REVIEW_AGENT_NAME] = manim_coding_review_agent
    
    code_exec_instruct_agent = ConversableAgent(
        name=CODE_EXEC_INSTRUCT_AGENT_NAME,
        system_message=prompts.get_code_exec_instruct_agent_prompt(),
        llm_config=llm_config,
        code_execution_config=False,
        human_input_mode="NEVER",
    )
    agents[CODE_EXEC_INSTRUCT_AGENT_NAME] = code_exec_instruct_agent

    # work_dir = Path("coding")
    work_dir = Path("../website/src/assets")
    work_dir.mkdir(exist_ok=True)

    
    class FixedFileExecutor(LocalCommandLineCodeExecutor):
        def create_file(self, code: str, filename: str) -> str:
            filepath = os.path.join(self.work_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)
            return filepath
        
        # @override
        def execute_code_blocks(self, code_blocks: List[CodeBlock]):
            # Create fixed files for each block
            for i, block in enumerate(code_blocks):
                if block.language == "python":
                    print("Creating python file")
                    self.create_file(block.code, "animation.py")
                elif block.language == "bash":
                    print("Creating manim creation script...")
                    self.create_file(block.code, "generate.sh")
                    # Make the bash script executable
                    os.chmod(os.path.join(self.work_dir, "generate.sh"), 0o755)
            
            print("Executing code...")
            return super().execute_code_blocks(code_blocks)
    
    # executor = LocalCommandLineCodeExecutor(work_dir=work_dir)
    executor = FixedFileExecutor(work_dir=work_dir)

    code_exec_agent = ConversableAgent(
        name=CODE_EXEC_AGENT_NAME,
        system_message=prompts.get_code_exec_agent_prompt(),
        llm_config=llm_config,
        code_execution_config={
            "executor": executor,
            "last_n_messages": 1,
        },
        human_input_mode="NEVER",
    )
    agents[CODE_EXEC_AGENT_NAME] = code_exec_agent
        
    
    groupchat = GroupChat(
        agents=[init_agent, textbook_agent, manim_coding_agent, manim_coding_review_agent, code_exec_instruct_agent, code_exec_agent],
        messages=[],
        max_round=20,
        speaker_selection_method=state_transition
    )
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    chat_result = init_agent.initiate_chat(
        manager,
        message="Here is the textbook text:\n" + user_query + "Please give a description of one detail that can be animated."
    )
    
    return chat_result


# if __name__ == "__main__":
#     with open("linear_equations_text.txt", "r") as f:
#         prompt = f.read()
#         main(prompt)

    # RAG TESTING - DOES NOT WORK
    # manim_docs_agent_prompt = "Assistant who has content retrieval power for the reference documentation of Manim Community Edition v0.18.1."
    # manim_docs_agent = RetrieveUserProxyAgent(
    #     name="Manim Docs Agent",
    #     retrieve_config={
    #         "task": "qa",
    #         "docs_path": "./rag/reference/",
    #         "system_message": manim_docs_agent_prompt,
    #     },
    #     human_input_mode="NEVER",
    # )

    # def retrieve_content(
    #     message: Annotated[
    #         str,
    #         "Refined message which keeps the original meaning and can be used to retrieve content for code generation and question answering.",
    #     ],
    #     n_results: Annotated[int, "number of results"] = 3,
    # ) -> str:
    #     manim_docs_agent.n_results = n_results  # Set the number of results to be retrieved.
    #     _context = {"problem": message, "n_results": n_results}
    #     ret_msg = manim_docs_agent.message_generator(manim_docs_agent, None, _context)
    #     return ret_msg or message

    # for caller in [textbook_agent, manim_agent]:
    #     d_retrieve_content = caller.register_for_llm(
    #     description="retrieve content for animation suggestions and code generation.", api_style="function"
    # )(retrieve_content)

    # for executor in [entrypoint_agent, textbook_agent, manim_agent]:
    #     executor.register_for_execution()(d_retrieve_content)
