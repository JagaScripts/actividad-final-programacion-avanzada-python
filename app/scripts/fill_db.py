import requests

from sqlalchemy.orm import Session

# Importar los modelos y la configuración de la base de datos
from app.core.database import SessionLocal, engine, Base
from app.models.user_model import User
from app.models.product_model import Product
from app.models.cart_model import CartItem

# URLs de la Fake Store API
FAKESTORE_API_URL_PRODUCTS = "https://fakestoreapi.com/products"
FAKESTORE_API_URL_USERS = "https://fakestoreapi.com/users"    
FAKESTORE_API_URL_CARTS = "https://fakestoreapi.com/carts" 

def fetch_data_from_api(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def create_tables():
    Base.metadata.create_all(bind=engine)

def fill_database():
    db = SessionLocal()
    try:
        # Obtener datos de la API y llenar la base de datos
        products = fetch_data_from_api(FAKESTORE_API_URL_PRODUCTS)
        users = fetch_data_from_api(FAKESTORE_API_URL_USERS)
        carts = fetch_data_from_api(FAKESTORE_API_URL_CARTS)

        # Llenar la tabla de productos
        for product in products:
            db.add(Product(**product))

        # Llenar la tabla de usuarios
        for user in users:
            db.add(User(**user))

        # Llenar la tabla de carritos
        for cart in carts:
            db.add(CartItem(**cart))

        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error al llenar la base de datos: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_tables()
    fill_database()