from fastapi import FastAPI
import asyncio
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
@app.get("/index")
async def read_index():
    data = {
        "message": "Hello, World!",
        "status": "success"
    }
    return JSONResponse(content=data)

@app.get("/text")
async def read_index():
    data = {
        "message": "Hello, text!",
        "status": "success"
    }
    return JSONResponse(content=data)

@app.get("/sleep")
async def read_sleep():
    await asyncio.sleep(10)
    data = {
        "message": "Slept for 10 seconds",
        "status": "success"
    }
    return JSONResponse(content=data)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
