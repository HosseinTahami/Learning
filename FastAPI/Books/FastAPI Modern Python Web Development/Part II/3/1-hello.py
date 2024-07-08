from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def greet():
    return "Hello? World?"

"""
$ http -v localhost:8000/hi  

    GET /hi HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Host: localhost:8000
    User-Agent: HTTPie/3.2.2



    HTTP/1.1 200 OK
    content-length: 15
    content-type: application/json
    date: Sat, 06 Jul 2024 10:38:38 GMT
    server: uvicorn

    "Hello? World?"
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("1-hello:app", reload=True)