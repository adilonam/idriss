# main.py

from fastapi import FastAPI

from pydantic import BaseModel
import os
import dill as pickle

app = FastAPI()

#load chain
model_id = "google/flan-t5-small"
directory_path = f'./data/{model_id}/dill/'

file_path = os.path.join(directory_path, 'chain.dill')

with open(file_path, 'rb') as f:
    chain = pickle.load(f)




class Item(BaseModel):
    query: str
    

@app.post("/v1/")
async def create_item(item: Item):
    print("processing ...")
    response  = chain.invoke(item.query)
    print("end processing")
    return {"response_str": response, "response_id": 123}