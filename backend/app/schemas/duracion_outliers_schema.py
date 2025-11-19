from typing import List, Optional
from pydantic import BaseModel


class CausaOutlierItem(BaseModel):
    """Item individual de causa outlier"""
    numero_expediente: str
    caratula: Optional[str]
    tribunal: Optional[str]
    estado_procesal: Optional[str]
    fecha_inicio: Optional[str]
    fecha_ultimo_movimiento: Optional[str]
    duracion_dias: int
    imputado_nombre: Optional[str]  # Nombre del imputado (denunciado)

    class Config:
        from_attributes = True


class DatosGraficoDuracionOutliers(BaseModel):
    """Datos del gráfico de outliers de duración"""
    causas_mas_largas: List[CausaOutlierItem]
    causas_mas_cortas: List[CausaOutlierItem]


class DuracionOutliersResponse(BaseModel):
    """Respuesta del endpoint de outliers de duración"""
    datos_grafico: DatosGraficoDuracionOutliers

    class Config:
        from_attributes = True

