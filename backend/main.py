import fastapi 
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def main() -> PlainTextResponse:
    return PlainTextResponse("Hello, World!")

