from app.api import routes_sign
from fastapi import FastAPI

app = FastAPI(
    title="Digital Signature Service",
    version="0.1.0",
    description="Toy digital signature service",
)

app.include_router(routes_sign.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Digital Signature Service running."}
