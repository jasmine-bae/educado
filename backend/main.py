from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
#ADD Import statements from the other files here
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific origins, e.g., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Or restrict to specific methods like ["POST"]
    allow_headers=["*"],  # Or restrict to specific headers like ["Content-Type"]
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/new_anim")
async def new_animation(file: UploadFile):
    print (file.filename)
    video_path = "assets/SquareAndSquareRoots.mp4"
    return {"video_path" : video_path}
