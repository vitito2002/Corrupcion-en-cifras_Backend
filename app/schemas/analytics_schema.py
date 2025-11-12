from pydantic import BaseModel
from typing import List
from app.schemas.expediente_schema import ExpedienteResponse


class CasosPorEstadoProcesalResponse(BaseModel):
    """Schema de respuesta para casos por estado procesal"""
    estado_procesal: str
    total: int
    casos: List[ExpedienteResponse]
    
    class Config:
        from_attributes = True


class EstadisticasEstadoProcesalResponse(BaseModel):
    """Schema de respuesta para estadísticas de estado procesal"""
    total: int
    en_tramite: int
    terminada: int
    porcentaje_en_tramite: float
    porcentaje_terminada: float
