from typing import Generator, List
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.causas_por_fuero_schema import (
    CausasPorFueroResponse,
    DatosGraficoCausasPorFuero,
    FueroCausaItem
)


class CausasPorFueroService:
    """
    Service para el gráfico de causas por fuero.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_grafico(self) -> CausasPorFueroResponse:
        """
        Obtiene datos agregados de causas por fuero listos para graficar.
        
        Returns:
            CausasPorFueroResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de fueros
        - data: Lista de cantidad de causas por fuero
        - fueros: Lista de objetos con fuero y cantidad
        - total_causas: Total general de causas
        """
        # Obtener datos del repository
        fueros_data = self.expediente_repository.get_causas_por_fuero()
        
        # Procesar datos para el gráfico
        labels = []
        data = []
        fueros_items = []
        
        # Calcular total
        total_causas = sum(item['cantidad_causas'] for item in fueros_data)
        
        for item in fueros_data:
            labels.append(item['fuero'])
            data.append(item['cantidad_causas'])
            
            # Crear item completo
            fueros_items.append(FueroCausaItem(
                fuero=item['fuero'],
                cantidad_causas=item['cantidad_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoCausasPorFuero(
            labels=labels,
            data=data,
            fueros=fueros_items,
            total_causas=total_causas
        )
        
        return CausasPorFueroResponse(datos_grafico=datos_grafico)


def get_causas_por_fuero_service(
    expediente_repo: ExpedienteRepository
) -> Generator[CausasPorFueroService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del CausasPorFueroService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de CausasPorFueroService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/causas-por-fuero")
        def get_causas(
            service: CausasPorFueroService = Depends(get_causas_por_fuero_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield CausasPorFueroService(expediente_repo)

