from fastapi import FastAPI

from app.routes.products import router as products_router
from app.routes.stores import router as stores_router


app = FastAPI()


app.include_router(products_router)
app.include_router(stores_router)


@app.get("/")
def root():
    return {
        "message": "Price Comparison API is running"
    }