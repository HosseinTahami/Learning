from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/happy", status_code=200)
def get_agent(status_code=201):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name: str, value:str, response:Response):
    response.headers[name] = value
    return "normal body..."


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("happy:app", reload=True)