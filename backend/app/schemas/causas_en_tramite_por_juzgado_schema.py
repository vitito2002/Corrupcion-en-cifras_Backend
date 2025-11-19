from pydantic import BaseModel
from typing import List


class JuzgadoCausasItem(BaseModel):
    """Schema para un item individual de juzgado con cantidad de causas en trámite"""
    tribunal: str
    cantidad_causas_en_tramite: int

    class Config:
        from_attributes = True


class DatosGraficoCausasEnTramitePorJuzgado(BaseModel):
    """Schema con datos listos para graficar causas en trámite por juzgado"""
    labels: List[str]  # Nombres de los juzgados/tribunales
    data: List[int]  # Cantidad de causas en trámite por juzgado
    juzgados: List[JuzgadoCausasItem]  # Lista de objetos con tribunal y cantidad
    total_causas_en_tramite: int  # Total general de causas en trámite


class CausasEnTramitePorJuzgadoResponse(BaseModel):
    """Schema de respuesta para causas en trámite por juzgado - formato listo para gráficos"""
    datos_grafico: DatosGraficoCausasEnTramitePorJuzgado

    class Config:
        from_attributes = True

