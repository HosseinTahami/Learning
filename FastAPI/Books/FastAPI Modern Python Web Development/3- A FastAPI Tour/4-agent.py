from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("agent:app", reload=True)

"""
$ http -v localhost:8000/agent who:hossein

    GET /agent HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Host: localhost:8000
    User-Agent: HTTPie/3.2.2
    who: hossein



    HTTP/1.1 200 OK
    content-length: 14
    content-type: application/json
    date: Fri, 05 Jul 2024 02:56:08 GMT
    server: uvicorn

    "HTTPie/3.2.2"
"""