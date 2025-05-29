from fastapi import FastAPI
from app.api.book import router as book_router
from app.api.user import router as user_router
from app.api.reader import router as reader_router

app = FastAPI()
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(reader_router, prefix="/readers", tags=["Readers"])


@app.get("/")
async def api_status():
    return {"status": "ok"}
