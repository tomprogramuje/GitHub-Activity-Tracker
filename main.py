from fastapi import FastAPI
from fastapi.responses import JSONResponse

import api

app = FastAPI()

default_token = "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"


@app.get("/")
async def home() -> JSONResponse:
    data = api.handle_home()
    response = {"message": data}
    return JSONResponse(content=response)


@app.get("/events")
async def get_events(repo_name: str, access_token: str | None = default_token) -> JSONResponse:
    data = api.handle_get_events(repo_name, access_token)
    return JSONResponse(content=data)
