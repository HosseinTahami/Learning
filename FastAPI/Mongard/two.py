from fastapi import FastAPI

app = FastAPI()

@app.get('/{name}/{age}') # localhost:8000/hossein/23
def info(name:str, age:int):
    return {"message":f"{name} is {age} years old !"}
"""
$ http -v localhost:8000/hossein/23         
    GET /hossein/23 HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate, br, zstd
    Connection: keep-alive
    Host: localhost:8000
    User-Agent: HTTPie/3.2.2



    HTTP/1.1 200 OK
    content-length: 39
    content-type: application/json
    date: Sat, 06 Jul 2024 13:43:27 GMT
    server: uvicorn

    {
        "message": "hossein is 23 years old !"
    }
"""

@app.get('/{name}') # localhost:8000/hossein?age=23
def info(name:str, age:int=0):
    return {"message":f"{name} is {age} years old !"}

"""
http -v localhost:8000/hossein age==23
GET /hossein?age=23 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br, zstd
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/3.2.2



HTTP/1.1 200 OK
content-length: 39
content-type: application/json
date: Sat, 06 Jul 2024 13:47:11 GMT
server: uvicorn

{
    "message": "hossein is 23 years old !"
}
"""