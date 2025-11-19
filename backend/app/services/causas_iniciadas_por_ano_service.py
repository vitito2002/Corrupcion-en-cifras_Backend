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
        Obtiene datos de causas iniciadas por año listos para graficar.
        
        Returns:
            CausasIniciadasPorAnoResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de años [2010, 2011, 2012, ...]
        - data: Lista de cantidad de causas por año [45, 67, 89, ...]
        - anos: Lista completa con todos los datos de cada año
        - total_causas: Total de causas en todos los años
        """
        # Obtener datos del repository
        datos_por_ano = self.expediente_repository.count_by_year()
        
        # Procesar datos para el gráfico
        labels = []
        cantidades = []
        anos_items = []
        
        # Calcular total
        total_causas = sum(item['cantidad_causas'] for item in datos_por_ano)
        
        for item in datos_por_ano:
            labels.append(item['anio'])
            cantidades.append(item['cantidad_causas'])
            
            # Crear item completo
            anos_items.append(AnioCausaItem(
                anio=item['anio'],
                cantidad_causas=item['cantidad_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoCausasPorAno(
            labels=labels,
            data=cantidades,
            anos=anos_items,
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

