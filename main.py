from fastapi import FastAPI
from os import environ as env
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/")
async def say_hello():
    return {"message": f"test env {env.get('My_key')} "}
