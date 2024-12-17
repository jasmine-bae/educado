### Educado

## Building for production

From the `website` folder

Install dependencies with `npm ci`

Run `npm run build`

From the `backend` folder

With Python version > 3.8
Create Python Virtual env and install dependencies
```
python -m venv manim_venv
source manin_venv/bin/activate
pip install -r requirements.txt
```

Run `fastapi run`

Access the website at `localhost:8000`

## Usage Instructions

Upload a `.txt` file with the instruction lesson