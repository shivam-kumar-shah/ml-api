from fastapi import FastAPI

from app.routers import heart_disease

app = FastAPI()

app.include_router(heart_disease.router)


@app.get("/")
async def root():
    return {"message": "Welcome to ml-api"}
