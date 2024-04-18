from fastapi import FastAPI
from fastapi.responses import JSONResponse

import api

app = FastAPI()


@app.get("/")
async def home() -> JSONResponse:
    data = api.handle_home()
    response = {"message": data}
    return JSONResponse(response)
