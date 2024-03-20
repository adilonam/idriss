# main.py

from fastapi import FastAPI

from pydantic import BaseModel
import os
import dill as pickle
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#load chain
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
directory_path = f'./data/{model_id}/dill/'

file_path = os.path.join(directory_path, 'chain.dill')

with open(file_path, 'rb') as f:
    chain = pickle.load(f)




class Item(BaseModel):
    user_input: str
    

@app.post("/v1/")
async def create_item(item: Item):
    print("processing ...")
    response  = chain.invoke(item.user_input)
    print("end processing")
    return {"message": response, "response_id": 123}