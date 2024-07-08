from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def greet():
    await asyncio.sleep(3)
    return "Hello! World!"