from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Price Comparison API is running"
    }