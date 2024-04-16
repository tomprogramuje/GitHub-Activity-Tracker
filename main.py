from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def home():
    data = {"message": "Hello World!"}
    return JSONResponse(content=data)
