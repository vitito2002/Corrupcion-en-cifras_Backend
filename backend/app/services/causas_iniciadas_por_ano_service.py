from typing import Generator
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.causas_iniciadas_por_ano_schema import (
    CausasIniciadasPorAnoResponse,
    DatosGraficoCausasPorAno,
    AnioCausaItem
)


class CausasIniciadasPorAnoService:
    """
    Service para el gráfico de causas iniciadas por año.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_grafico(self) -> CausasIniciadasPorAnoResponse:
        """
        Obtiene datos de causas iniciadas por año listos para graficar, separadas por estado.
        
        Returns:
            CausasIniciadasPorAnoResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de años [2010, 2011, 2012, ...]
        - causas_abiertas: Lista de cantidad de causas abiertas por año
        - causas_terminadas: Lista de cantidad de causas terminadas por año
        - data: Lista de cantidad total de causas por año (para compatibilidad)
        - anos: Lista completa con todos los datos de cada año
        - totales: Totales de causas abiertas, terminadas y total
        """
        # Obtener datos del repository
        datos_por_ano = self.expediente_repository.count_by_year()
        
        # Procesar datos para el gráfico
        labels = []
        causas_abiertas = []
        causas_terminadas = []
        cantidades = []
        anos_items = []
        
        # Calcular totales
        total_causas_abiertas = sum(item['cantidad_causas_abiertas'] for item in datos_por_ano)
        total_causas_terminadas = sum(item['cantidad_causas_terminadas'] for item in datos_por_ano)
        total_causas = sum(item['cantidad_causas'] for item in datos_por_ano)
        
        for item in datos_por_ano:
            labels.append(item['anio'])
            causas_abiertas.append(item['cantidad_causas_abiertas'])
            causas_terminadas.append(item['cantidad_causas_terminadas'])
            cantidades.append(item['cantidad_causas'])
            
            # Crear item completo
            anos_items.append(AnioCausaItem(
                anio=item['anio'],
                cantidad_causas_abiertas=item['cantidad_causas_abiertas'],
                cantidad_causas_terminadas=item['cantidad_causas_terminadas'],
                cantidad_causas=item['cantidad_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoCausasPorAno(
            labels=labels,
            causas_abiertas=causas_abiertas,
            causas_terminadas=causas_terminadas,
            data=cantidades,
            anos=anos_items,
            total_causas_abiertas=total_causas_abiertas,
            total_causas_terminadas=total_causas_terminadas,
            total_causas=total_causas
        )
        
        return CausasIniciadasPorAnoResponse(datos_grafico=datos_grafico)


def get_causas_iniciadas_por_ano_service(
    expediente_repo: ExpedienteRepository
) -> Generator[CausasIniciadasPorAnoService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del CausasIniciadasPorAnoService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de CausasIniciadasPorAnoService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/causas-iniciadas-por-ano")
        def get_causas(
            service: CausasIniciadasPorAnoService = Depends(get_causas_iniciadas_por_ano_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield CausasIniciadasPorAnoService(expediente_repo)

