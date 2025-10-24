# actividad-final-programacion-avanzada-python
Repositorio para aplicar principios POO y SOLID, donde se desarrolla y despliega aplicaciones web backend con FastAPI y requests para consumirla

## 🚀 Instalación y Configuración

### 1. Crear y activar entorno virtual
```bash
python -m venv env_fastapi
source env_fastapi/bin/activate  # Linux/Mac
# o
env_fastapi\Scripts\activate    # Windows
```
### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 3. Ejecutar la API
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
La API estará disponible en: http://localhost:8000

### 4. Documentación automática
Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

### 5. 🧪 Testing
Ejecutar tests automáticos no te preocupes por si se te ha olvidado:
La base de datos, los tests se encargan de crear y eliminar la base de datos de prueba automáticamente.
Arrancar la API, los tests se encargan de iniciar la API automáticamente.
```bash
python scripts/test_api.py
```



