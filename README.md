### Educado

Educado is an LLM agent powered application designed to turn textbook material, educational blog posts, worksheets, and more into animated lessons/learning material. Currently, we only support mathematics lesson / textbook text input into animated math videos. We utilize a finite-state-machine to power agentic group chat to create directions, generate/review Python code powered by the Manim Community library, and execute rendering of the video.

```mermaid
---
config:
  theme: mc
  look: neo
  layout: fixed
---
flowchart LR
    n1["Init_Agent<br>(starts conversation)"] --> n2["Textbook Agent<br>(creates English instructions for a math animation related/derived from lesson concepts with Manim in mind)"]
    n3["User: Text of math lesson"] --> n1
    n2 --> n4["Coding Agent<br>(generates Python + Manim code)"]
    n4 --> n5["Coding Review Agent<br>(reviews code and outputs if changes are needed + suggestions)"]
    n5 --> n10["Execution Instruction Agent<br>(generates any bash scripts to run code)"] & n8["Changes needed?"]
    n10 --> n11["Code Execution Agent<br>(executes code and renders animation)"]
    n11 --> n12["Code Errored?"] & n13["Video Generated"]
    n8 --> n4
    n12 --> n5
    n1@{ shape: rounded}
    n3@{ shape: rounded}
    n8@{ shape: out-in}
    n12@{ shape: out-in}
    n13@{ shape: rounded}
     n3:::Pine
     n13:::Pine
    classDef Pine stroke-width:1px, stroke-dasharray:none, stroke:#254336, fill:#27654A, color:#FFFFFF
    style n8 fill:#BBDEFB
    style n12 fill:#BBDEFB
```
## Installation
Create a python virtual environment named `manim_venv` with requirements.txt.
```
python -m venv manim_venv
source manim_venv/bin/activate
pip install -r requirements.txt
```

For a working `Manim Community v0.18.1` installation you may require additional system packages to be installed.

Instructions for your platform (Mac, Linux, etc) can be found here: https://docs.manim.community/en/stable/installation.html

**Note:** This includes the optional dependencies listed further down the page like LaTeX for equation generation, etc


You must add an OpenAI API key in your venv.
`export OPENAI_API_KEY=sk-proj-your-openai-api-key-here`

(Optional) Add a Claude API key as well. If you set this, it will use Claude for the coding/code review steps of the process. We found during testing that Claude 3.5 Sonnet tends to perform better on the coding and review portion of the process.
`export CLAUDE_API_KEY=sk-ant-your-anthropic-api-key`

This program should cost no more than 10 cents to run each time. Ensure you have enough credits or generation may fail.

These steps have been tested on Mac and Ubuntu (WSL)

## Building for production

From the `website` folder

Install dependencies with `npm ci`

Run `npm run build`

From the `backend` folder

Make sure you are using the `manim_venv` virtual enviroment

Run `fastapi run`

Access the website at `localhost:8000`

## Usage Instructions

1. Upload a `.txt` file with the math instruction lesson.
2. Click generate and wait for the generation agent to run. You can monitor the progress on your terminal running the `fastapi` server
3. Once the process is complete, the video will display on the web page. You can right click and save the video if you want to keep the result!