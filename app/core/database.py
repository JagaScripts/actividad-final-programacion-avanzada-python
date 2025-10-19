# app/core/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión para la base de datos SQLite.
DATABASE_URL = "sqlite:///./fakestore.db"

# 'engine' es el objeto que maneja la conexión a la base de datos.
# Aquí estamos creando un motor de base de datos SQLite.
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal será la clase que usaremos para crear las sesiones de la base de datos.
# Cada instancia de SessionLocal será una sesión de base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 'Base' es una clase base de la que heredarán todos nuestros modelos de SQLAlchemy.
# SQLAlchemy usa esta clase para mapear los modelos a las tablas de la base de datos.
Base = declarative_base()