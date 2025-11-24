from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func
from app.core.database import Base


class Metadata(Base):
    """
    Modelo SQLAlchemy para la tabla metadata.
    Almacena metadatos del sistema, como la fecha de última actualización.
    """
    __tablename__ = "metadata"
    
    # Primary Key
    clave = Column(String(50), primary_key=True)
    
    # Valor (puede ser fecha, texto, etc.)
    valor = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    def __repr__(self):
        return f"<Metadata(clave='{self.clave}', valor='{self.valor}')>"

