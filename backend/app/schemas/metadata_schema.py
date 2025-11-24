from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UltimaActualizacionResponse(BaseModel):
    """Schema de respuesta para la fecha de última actualización"""
    ultima_actualizacion: Optional[datetime]
    formato_fecha: str  # Fecha formateada para mostrar
    
    class Config:
        from_attributes = True

