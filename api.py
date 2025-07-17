from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Настраиваем работу с шаблонами
templates = Jinja2Templates(directory="templates")

# Путь к директории с файлами
FILE_DIRECTORY = "/opt/container"

@app.get("/")
async def read_root(request: Request):
    try:
        # Получаем список файлов
        files = os.listdir(FILE_DIRECTORY)
    except FileNotFoundError:
        files = []
    
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request, 
            "files": files
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
