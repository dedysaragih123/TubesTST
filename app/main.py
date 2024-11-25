from fastapi import FastAPI, Depends
from app.routers import secure, public
from app.auth import get_user
import logging

app = FastAPI()

app.include_router(
    public.router,
    prefix="/api/v1/public"
)
app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)

@app.on_event("startup")
async def startup_event():
    logging.info("Application is starting up...")

@app.get("/")
async def read_root():
    logging.info("Root endpoint accessed.")
    return {"message": "Hello, world!"}