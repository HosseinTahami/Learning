from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World - GET METHOD"}


@app.post("/")
def index():
    return {"message": "Hello World - POST METHOD"}
