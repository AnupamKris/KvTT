# from fastapi import FastAPI
from jarvis import process_text
'''from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
async def root():
    ret = process_text("hello")
    return HTMLResponse("index.html", 200)
'''

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse  

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api")
async def api(request: Request):
    data = await request.json()
    query = data['text']

    ret = process_text(query)
    print(ret)
    return JSONResponse(content={"message": "Item created", "text": ret})