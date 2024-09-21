from fastapi import FastAPI

from config import config


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config.app.host, port=config.app.port, log_level=config.app.loglevel)


