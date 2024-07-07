from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, status, Request, responses

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/home/{username}", response_class=responses.HTMLResponse)
def index(request: Request, username:str):
    return templates.TemplateResponse("home.html", {"request": request, "username":username})
