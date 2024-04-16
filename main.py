from fastapi import FastAPI
from fastapi.responses import JSONResponse

import api

app = FastAPI()


@app.get("/")
async def home():
    data = api.handle_home()
    response = {"message": data}
    return JSONResponse(content=response)
