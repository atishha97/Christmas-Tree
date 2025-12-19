"""
The Holiday Tree - FastAPI Backend
Serves the Vue.js frontend and handles static files
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path
import uvicorn

app = FastAPI(title="The Holiday Tree")

# Get the directory where main.py is located
BASE_DIR = Path(__file__).resolve().parent

# Mount static files
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.mount("/assets", StaticFiles(directory=BASE_DIR / "assets"), name="assets")


@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve the main application"""
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/tree/{tree_id}", response_class=HTMLResponse)
async def view_tree(tree_id: str):
    """Serve the tree view - same SPA, routing handled by Vue"""
    return FileResponse(BASE_DIR / "static" / "index.html")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
