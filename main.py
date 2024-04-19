from fastapi import FastAPI
from fastapi.responses import JSONResponse

import api

app = FastAPI()


@app.get("/")
async def home() -> JSONResponse:
    data = api.handle_home()
    response = {"message": data}
    return JSONResponse(content=response)


@app.get("/events/{owner_repo}")
async def events() -> JSONResponse:
    data = api.handle_events(owner_repo)
    return JSONResponse(content=data)
