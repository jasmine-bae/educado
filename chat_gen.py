from typing import Annotated, Dict, List
from autogen import ConversableAgent
from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import sys
import os
import math

# Do not modify the signature of the "main" function.
def main(user_query: str):

    entrypoint_agent_system_message = "Please take in any text or code in exactly and pass it to the next agent directly. Do not summarize any text or code yourself. Don't add any additional commentary."
    # example LLM config for the entrypoint agent
    llm_config = {"config_list": [{"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}]}
    # the main entrypoint/supervisor agent
    entrypoint_agent = ConversableAgent("entrypoint_agent", 
                                        system_message=entrypoint_agent_system_message, 
                                        llm_config=llm_config)


    textbook_agent_prompt = "Please take in this text from a math textbook and create a description around any visual concepts that should be represented as visualization/animation in Manim Community v0.18.0.post0. The description must only contain info about the visuals and is constrained available tools/classes in the manim library,"
    textbook_agent = ConversableAgent("textbook_agent", 
                                        system_message=textbook_agent_prompt, 
                                        llm_config=llm_config,
                                        max_consecutive_auto_reply=0,
                                        human_input_mode="NEVER")
    # TODO
    # Create more agents here. 
    manim_agent_prompt = "You are an expert in creating math animations using the python library, Manim Community v0.18.0.post0. Please generate a script in python according to user prompt. Focus on correctness of the python and manim code. Do not output anything but the python code. Take a deep breath and go."
    manim_agent = ConversableAgent("manim_agent", 
                                        system_message=manim_agent_prompt, 
                                        llm_config=llm_config,
                                        max_consecutive_auto_reply=1,
                                        human_input_mode="NEVER")

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


    result = entrypoint_agent.initiate_chats([
        {
            "recipient": textbook_agent,
            "message": "Here is the textbook text" + user_query + "'. , please give me the description for one math animation that should be represented in detail.",
            "summary_prompt":"Return the description/prompt that will be used by an animator to create the math animation/visual. Do not add any introductory phrases.",
            "summary_method":"last_msg"
        }
        ,
        {
            "recipient": manim_agent,
            "message": "Here is animation description prompt given to you to make the manim python code.",
            "summary_prompt":"Return Python code that utilizes manim to create the math animation as closely as to the descripton above. Do not add any introductory phrases.",
            "summary_method":"last_msg"
        }
        ])
    return result


    
# DO NOT modify this code below.
if __name__ == "__main__":

    with open("textbook_text.txt", "r") as f:
        prompt = f.read()
        main(prompt)