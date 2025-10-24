import requests
import logging
import time

BASE_URL = "http://localhost:8000"
HEADERS = {"Content-Type": "application/json"}

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Metodo genérico para testear un endpoint
def test_endpoint(method, endpoint, expected_status, json_data=None, description=""):
    try:
        url = f"{BASE_URL}{endpoint}"
        logger.info(f"Testing {method} {endpoint} - {description}")
        
        response = requests.request(method, url, json=json_data, headers=HEADERS)
        
        # Assert para verificar el código de estado
        assert response.status_code == expected_status, f"Esperado {expected_status}, obtenido {response.status_code}"
        
        logger.info(f"✅ SUCCESS: Esperado {expected_status}, obtenido {response.status_code}")
        
        # Retornar response para más verificaciones
        return response
        
    except requests.exceptions.ConnectionError:
        logger.error(f"❌ CONNECTION ERROR: No se puede conectar a {BASE_URL}")
        raise
    except AssertionError as e:
        logger.error(f"❌ ASSERTION FAILED: {e}")
        logger.error(f"Response: {response.text}")
        raise
    except Exception as e:
        logger.error(f"❌ EXCEPTION: {e}")
        raise

def run_tests():
    """Ejecutar todos los tests con asserts"""
    logger.info("🚀 Iniciando tests de la API JaGaStore")
    
    # Esperar a que la API esté lista
    time.sleep(2)
    
    try:
        # 1. Test endpoints GET (lectura)
        logger.info("\n--- TESTING ENDPOINTS GET ---")
        
        # Health check
        test_endpoint("GET", "/health", 200, description="Health check")
        
        # Obtener todos los usuarios
        response = test_endpoint("GET", "/users/", 200, description="Obtener todos los usuarios")
        users = response.json()
        assert len(users) > 0, "Debe haber al menos un usuario"
        
        # Obtener usuario específico
        response = test_endpoint("GET", "/users/1", 200, description="Obtener usuario ID 1")
        user = response.json()
        assert user["id"] == 1, "Debe retornar el usuario con ID 1"
        
        # Obtener todos los productos
        response = test_endpoint("GET", "/products/", 200, description="Obtener todos los productos")
        products = response.json()
        assert len(products) > 0, "Debe haber al menos un producto"
        
        # Obtener productos por categoría
        response = test_endpoint("GET", "/products/?category=men's%20clothing", 200, description="Obtener productos por categoría")
        
        # Obtener todos los carritos
        response = test_endpoint("GET", "/carts/", 200, description="Obtener todos los carritos")
        carts = response.json()
        assert len(carts) > 0, "Debe haber al menos un carrito"
        
        # 2. Test endpoints POST (creación)
        logger.info("\n--- TESTING ENDPOINTS POST ---")
        
        # Crear nuevo usuario
        new_user = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "password123",
            "name": {"firstname": "Test", "lastname": "User"},
            "address": {
                "city": "Test City",
                "street": "Test Street", 
                "number": 123,
                "zipcode": "12345",
                "geolocation": {"lat": "0.0", "long": "0.0"}
            },
            "phone": "1-234-567-890"
        }
        
        response = test_endpoint("POST", "/users/", 201, json_data=new_user, description="Crear nuevo usuario")
        created_user = response.json()
        new_user_id = created_user["id"]
        assert created_user["email"] == "test@example.com", "Email del usuario creado debe coincidir"
        
        # 3. Test endpoints PUT (actualización)
        logger.info("\n--- TESTING ENDPOINTS PUT ---")
        
        # Actualizar usuario
        update_user = {
            "phone": "1-999-888-777"
        }
        
        response = test_endpoint("PUT", "/users/1", 200, json_data=update_user, description="Actualizar usuario")
        updated_user = response.json()
        assert updated_user["phone"] == "1-999-888-777", "Teléfono debe estar actualizado"
        
        # 4. Test endpoints DELETE (eliminación)
        logger.info("\n--- TESTING ENDPOINTS DELETE ---")
        
        # Eliminar usuario creado
        test_endpoint("DELETE", f"/users/{new_user_id}", 204, description="Eliminar usuario creado")
        
        # 5. Test casos de error
        logger.info("\n--- TESTING CASOS DE ERROR ---")
        
        # Usuario no existente
        test_endpoint("GET", "/users/999", 404, description="Usuario no existente")
        
        # Producto no existente  
        test_endpoint("GET", "/products/999", 404, description="Producto no existente")
        
        logger.info("🎉 ¡Todos los tests pasaron correctamente!")
        
    except Exception as e:
        logger.error(f"💥 Tests fallaron: {e}")
        raise

if __name__ == "__main__":
    run_tests()