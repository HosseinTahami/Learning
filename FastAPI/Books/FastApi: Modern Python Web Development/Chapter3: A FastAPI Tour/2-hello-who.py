from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/hi/{who}/")  # localhost:9000/hi/kevin/
def greet(who):
    return f"Hello? {who}?"




@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"  # localhost:9000/hi?who=kevin

"""
$ http -v localhost:9000/hi who==ali

GET /hi?who=ali HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:9000
User-Agent: HTTPie/3.2.2



HTTP/1.1 200 OK
content-length: 13
content-type: application/json
date: Thu, 04 Jul 2024 10:20:26 GMT
server: uvicorn

"Hello? ali?"
"""

@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}?"
"""
$ http -v localhost:9000/hi who=ali 

POST /hi HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 14
Content-Type: application/json
Host: localhost:9000
User-Agent: HTTPie/3.2.2

{
    "who": "ali"
}


HTTP/1.1 200 OK
content-length: 13
content-type: application/json
date: Thu, 04 Jul 2024 10:20:30 GMT
server: uvicorn

"Hello? ali?"

"""

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello-who:app", reload=True, port=9000)
