from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def api_status():
    return {"status": "ok"}