from sqlalchemy import Column, String, Text, Date, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import date

from app.core.database import Base


class Expediente(Base):
    """
    Modelo SQLAlchemy para la tabla expediente.
    Representa un expediente judicial de corrupción.
    """
    __tablename__ = "expediente"
    
    # Primary Key
    numero_expediente = Column(String(50), primary_key=True)
    
    # Campos de texto
    caratula = Column(Text, nullable=True)
    jurisdiccion = Column(Text, nullable=True)
    tribunal = Column(Text, nullable=True)  # Redundancia textual
    camara_origen = Column(Text, nullable=True)
    delitos = Column(Text, nullable=True)
    fiscal = Column(Text, nullable=True)
    fiscalia = Column(Text, nullable=True)
    
    # Estado procesal con constraint
    estado_procesal = Column(
        String(50),
        CheckConstraint("estado_procesal IN ('En trámite', 'Terminada')", name='check_estado_procesal'),
        nullable=True
    )
    
    # Fechas
    fecha_inicio = Column(Date, nullable=True)
    fecha_ultimo_movimiento = Column(Date, nullable=True)
    
    # Año de inicio
    ano_inicio = Column(Integer, nullable=True)
    
    # Nota: La tabla expediente NO tiene id_tribunal como FK.
    # Se relaciona con tribunal usando el campo TEXT tribunal con tribunal.nombre
    
    def __repr__(self):
        return f"<Expediente(numero_expediente='{self.numero_expediente}', estado='{self.estado_procesal}')>"
