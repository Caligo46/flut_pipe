import uvicorn   # pip install uvicorn 
from fastapi import FastAPI   # pip install fastapi 
import random

# Create the FastAPI application
app = FastAPI()

# A simple example of a GET request
@app.get("/")
def read_root():
    return "Hello World!"

@app.get('/example')
def root():
    return {"example":"This is example", "data": 23}

@app.get('/example/random')
def get_random():
    rn = random.randint(0,100)
    return {"number": rn, "limit": "100"}

@app.get('/example/random/{limit}')
def get_random(limit:int):
    rn = random.randint(0,limit)
    return {"number": rn, "limit": limit}

# Run the server
if __name__ == "__main__":
    uvicorn.run("api_test:app",
            reload= True,   # Reload the server when code changes
            host="127.0.0.1",   # Listen on localhost 
            port=5000,   # Listen on port 5000 
            log_level="info"   # Log level
            )
