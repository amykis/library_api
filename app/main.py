from fastapi import FastAPI
from app.api.book import router as book_router
from app.api.user import router as user_router

app = FastAPI()
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(user_router, prefix="/users", tags=["Users"])


@app.get("/")
async def api_status():
    return {"status": "ok"}
