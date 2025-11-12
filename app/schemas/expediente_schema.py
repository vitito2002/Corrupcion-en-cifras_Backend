from pydantic import BaseModel
from typing import Optional
from datetime import date


class ExpedienteBase(BaseModel):
    """Schema base para Expediente"""
    numero_expediente: str
    caratula: Optional[str] = None
    jurisdiccion: Optional[str] = None
    tribunal: Optional[str] = None
    estado_procesal: Optional[str] = None
    fecha_inicio: Optional[date] = None
    fecha_ultimo_movimiento: Optional[date] = None
    camara_origen: Optional[str] = None
    ano_inicio: Optional[int] = None
    delitos: Optional[str] = None
    fiscal: Optional[str] = None
    fiscalia: Optional[str] = None
    id_tribunal: Optional[int] = None


class ExpedienteResponse(ExpedienteBase):
    """Schema de respuesta para Expediente"""
    
    class Config:
        from_attributes = True
