import os
import sys

# Define the folder structure and content for each file
structure = {
    "main.py": '''# main.py
from fastapi import FastAPI
from supabase import create_client
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, EmailStr
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
''',
    "requirements.txt": '''# requirements.txt
fastapi
uvicorn
supabase
python-dotenv
pydantic
jinja2
websockets
werkzeug
requests
''',
    ".env": '''# .env
FLASK_APP=main.py
FLASK_ENV=development
''',
    "templates/index.html": "<h1>Welcome to the Index Page</h1>",
    "templates/about.html": "<h1>About Us</h1>",
    "templates/page1.html": "<h1>This is Page 1</h1>",
    "templates/page2.html": "<h1>This is Page 2</h1>",
    "templates/page3.html": "<h1>This is Page 3</h1>",
    "templates/404.html": "<h1>404 - Page Not Found</h1>",
    "templates/parts/nav.html": "<nav><ul><li><a href='/'>Home</a></li></ul></nav>",
    "static/css/style.css": "body { font-family: Arial, sans-serif; }",
    "static/js/script.js": 'console.log("Welcome to the website!");',
    "data/database.db": "-- database.db\n-- This is a placeholder for your database file."
}

def create_structure(base_path):
    """Creates the folder structure and files based on the predefined structure dictionary."""
    for file_path, content in structure.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
    print(f"✅ Folder structure and files have been created successfully in: {base_path}")

def main():
    """Entry point for the command-line tool."""
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = input("Enter the path where you want to create the folder structure: ").strip()

    if not os.path.exists(base_path):
        os.makedirs(base_path)

    create_structure(base_path)

if __name__ == "__main__":
    main()
