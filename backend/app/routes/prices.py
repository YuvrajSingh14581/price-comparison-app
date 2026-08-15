from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.price import Price
from app.models.product import Product
from app.models.store import Store
from app.schemas.price import PriceCreate, PriceResponse


router = APIRouter(
    prefix="/prices",
    tags=["Prices"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PriceResponse)
def create_price(
    price: PriceCreate,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == price.product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    store = (
        db.query(Store)
        .filter(Store.id == price.store_id)
        .first()
    )

    if not store:
        raise HTTPException(
            status_code=404,
            detail="Store not found"
        )

    new_price = Price(
        product_id=price.product_id,
        store_id=price.store_id,
        price=price.price,
        original_price=price.original_price,
        currency=price.currency,
        product_url=price.product_url,
        availability=price.availability
    )

    db.add(new_price)
    db.commit()
    db.refresh(new_price)

    return new_price


@router.get("/", response_model=list[PriceResponse])
def get_prices(db: Session = Depends(get_db)):
    return db.query(Price).all()