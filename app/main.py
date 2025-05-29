from fastapi import FastAPI
from app.api.book import router as book_router

app = FastAPI()
app.include_router(book_router, prefix="/books", tags=["Books"])


@app.get("/")
async def api_status():
    return {"status": "ok"}
