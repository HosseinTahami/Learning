from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/agent")
def greet(who:str = Header()):
    return f"Hello? {who}?"