import uvicorn   # pip install uvicorn 
from fastapi import FastAPI   # pip install fastapi 
import random

# 예측 모듈 가져오기
import vgg16_prediction_model

# Create the FastAPI application
app = FastAPI()

# A simple example of a GET request
@app.get("/")
def read_root():
    return "VGG16모델을 사용하는 API를 만들어봅시다."

@app.get('/sample')
def sample_prediction():
    result = vgg16_prediction_model.prediction_model()
    return result


# Run the server
if __name__ == "__main__":
    uvicorn.run("inference:app",
            reload= True,   # Reload the server when code changes
            host="127.0.0.1",   # Listen on localhost 
            port=5000,   # Listen on port 5000 
            log_level="info"   # Log level
            )
