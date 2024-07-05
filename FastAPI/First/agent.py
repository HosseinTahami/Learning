from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("agent:app", reload=True)