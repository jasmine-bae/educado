### Educado

Educado is an LLM agent powered application designed to turn textbook material, educational blog posts, worksheets, and more into animated lessons/learning material. Currently, we only support mathematics lesson / textbook text input into animated math videos. We utilize a finite-state-machine to power agentic group chat to create directions, generate/review Python code powered by the Manim Community library, and execute rendering of the video.

## Installation
Create a python virtual environment with requirements.txt.

You must add an OpenAI API key in your venv.

(Optional) Add a Claude API key as well.

## Building for production

From the `website` folder

Run `npm run build`

From the `backend` folder

Run `fastapi run`

Access the website at `localhost:8000`

## Usage Instructions

Upload a `.txt` file with the math instruction lesson.