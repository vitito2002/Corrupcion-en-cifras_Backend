from pydantic import BaseModel
from typing import List


class JuzgadoCausasItem(BaseModel):
    """Schema para un item individual de juzgado con cantidad de causas"""
    tribunal: str
    cantidad_causas_abiertas: int
    cantidad_causas_terminadas: int
    cantidad_causas: int

    class Config:
        from_attributes = True


class DatosGraficoCausasEnTramitePorJuzgado(BaseModel):
    """Schema con datos listos para graficar causas por juzgado"""
    labels: List[str]  # Nombres de los juzgados/tribunales
    causas_abiertas: List[int]  # Cantidad de causas en trámite por juzgado
    causas_terminadas: List[int]  # Cantidad de causas terminadas por juzgado
    data: List[int]  # Cantidad total de causas por juzgado (para compatibilidad)
    juzgados: List[JuzgadoCausasItem]  # Lista de objetos con tribunal y cantidades
    total_causas_abiertas: int  # Total general de causas en trámite
    total_causas_terminadas: int  # Total general de causas terminadas
    total_causas_en_tramite: int  # Total general de causas en trámite (para compatibilidad)
    total_causas: int  # Total general de causas


class CausasEnTramitePorJuzgadoResponse(BaseModel):
    """Schema de respuesta para causas en trámite por juzgado - formato listo para gráficos"""
    datos_grafico: DatosGraficoCausasEnTramitePorJuzgado

    class Config:
        from_attributes = True

