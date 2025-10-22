import requests
import logging
from sqlalchemy.orm import Session 
from models.dec_base import DecBase
from core.database import SessionLocal, engine

# Constantes para la Fake Store API
FAKE_STORE_API_BASE_URL = "https://fakestoreapi.com"
PRODUCTS_ENDPOINT = f"{FAKE_STORE_API_BASE_URL}/products"
USERS_ENDPOINT = f"{FAKE_STORE_API_BASE_URL}/users" 
CARTS_ENDPOINT = f"{FAKE_STORE_API_BASE_URL}/carts"

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fakestore")

def get_items_model(model_url):
    try:
        response = requests.get(model_url)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        logger.error(f"Error al obtener datos de {model_url}: {e}")
        return None
    except requests.RequestException as e:
        logger.error(f"Error de conexión con {model_url}: {e}")
        return None

if __name__ == "__main__":
    # Test de la función
    products = get_items_model(PRODUCTS_ENDPOINT)
    if products:
        print(f"✅ Se obtuvieron {len(products)} productos")
        print("Primer producto:", products[0]['title'])
    else:
        print("❌ Error obteniendo productos")