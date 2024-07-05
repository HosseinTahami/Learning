from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/agent")
def greet(who:str = Header()):
    return f"Hello? {who}?"

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
    content-length: 17
    content-type: application/json
    date: Fri, 05 Jul 2024 02:57:16 GMT
    server: uvicorn

    "Hello? hossein?"
"""