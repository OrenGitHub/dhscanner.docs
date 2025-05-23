import fastapi

from fastapi.staticfiles import StaticFiles

app = fastapi.FastAPI()

app.mount("/docs", StaticFiles(directory="site", html=True), name="static")
