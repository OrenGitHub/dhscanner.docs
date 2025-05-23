import fastapi

from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = fastapi.FastAPI()

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs/")

app.mount("/docs", StaticFiles(directory="site", html=True), name="static")
