from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/agent")
def greet(who:str = Header()):
    return f"Hello? {who}?"

"""
$ http localhost:8000/agent who:hossein 

    HTTP/1.1 200 OK
    content-length: 17
    content-type: application/json
    date: Fri, 05 Jul 2024 02:53:33 GMT
    server: uvicorn

    "Hello? hossein?"
"""