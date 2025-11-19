from pydantic import BaseModel
from typing import List, Optional


class CausaDuracionItem(BaseModel):
    """Schema para un item individual de causa con su duración"""
    numero_expediente: str
    caratula: Optional[str]
    tribunal: Optional[str]
    estado_procesal: Optional[str]
    fecha_inicio: Optional[str]  # ISO format date string
    fecha_ultimo_movimiento: Optional[str]  # ISO format date string
    duracion_dias: int

    class Config:
        from_attributes = True


class DatosGraficoDuracionInstruccion(BaseModel):
    """Schema con datos listos para graficar duración de instrucción"""
    labels: List[str]  # Números de expediente o carátulas
    data: List[int]  # Duración en días
    causas: List[CausaDuracionItem]  # Lista completa de causas con todos los datos
    duracion_promedio_dias: float  # Duración promedio en días
    duracion_maxima_dias: int  # Duración máxima en días
    duracion_minima_dias: int  # Duración mínima en días
    total_causas: int  # Total de causas analizadas


class DuracionInstruccionResponse(BaseModel):
    """Schema de respuesta para duración de instrucción - formato listo para gráficos"""
    datos_grafico: DatosGraficoDuracionInstruccion

    class Config:
        from_attributes = True

