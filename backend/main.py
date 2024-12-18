from typing import Union
from fastapi import FastAPI, File, UploadFile,  Request
from fastapi.middleware.cors import CORSMiddleware
import chat_gen
from fastapi.responses import JSONResponse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

#ADD Import statements from the other files here
app = FastAPI()
# Allow the frontend to make requests to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or specify the frontend URL like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/new_anim")
async def new_animation(request: Request, file: UploadFile):
    
    headers = request.headers
    logging.info(f"Request Headers: {dict(headers)}")
    # print (file.filename)
    with open(file.filename, "r") as f:
        prompt = f.read()
        chat_gen.main(prompt)
        # return StreamingResponse(chat_gen.main(prompt), media_type="text/plain")

    # # video_path = result #change this
    return {"filename" : file.filename}
    # return JSONResponse(content={"status": "success", "message": "File processed"})
    # return {"message": "Processing started"}

