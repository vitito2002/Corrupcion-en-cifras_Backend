from typing import Generator
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.analytics_schema import CasosPorEstadoProcesalResponse
from app.schemas.expediente_schema import ExpedienteResponse


class AnalyticsService:
    """
    Service para lógica de negocio de analytics.
    Procesa datos del repository y los prepara para los routers.
    Este service está enfocado en casos por estado procesal.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_casos_por_estado_procesal(
        self,
        estado_procesal: str,
        skip: int = 0,
        limit: int = 100
    ) -> CasosPorEstadoProcesalResponse:
        """
        Obtiene casos filtrados por estado procesal.
        
        Args:
            estado_procesal: Estado procesal ('En trámite' o 'Terminada')
            skip: Número de registros a saltar (para paginación)
            limit: Número máximo de registros a retornar
            
        Returns:
            CasosPorEstadoProcesalResponse con los casos y el total
            
        Raises:
            ValueError: Si el estado_procesal no es válido
        """
        # Validar estado procesal
        estados_validos = ['En trámite', 'Terminada']
        if estado_procesal not in estados_validos:
            raise ValueError(
                f"Estado procesal inválido. Debe ser uno de: {', '.join(estados_validos)}"
            )
        
        # Obtener casos del repository
        casos = self.expediente_repository.get_by_estado_procesal(
            estado_procesal=estado_procesal,
            skip=skip,
            limit=limit
        )
        
        # Obtener total de casos con ese estado
        total = self.expediente_repository.count_by_estado_procesal(estado_procesal)
        
        # Convertir modelos SQLAlchemy a schemas Pydantic
        casos_response = [ExpedienteResponse.model_validate(caso) for caso in casos]
        
        # Preparar respuesta
        return CasosPorEstadoProcesalResponse(
            estado_procesal=estado_procesal,
            total=total,
            casos=casos_response
        )


def get_analytics_service(
    expediente_repo: ExpedienteRepository
) -> Generator[AnalyticsService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del AnalyticsService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de AnalyticsService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/casos-por-estado/{estado}")
        def get_casos(
            estado: str,
            service: AnalyticsService = Depends(get_analytics_service)
        ):
            return service.get_casos_por_estado_procesal(estado)
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield AnalyticsService(expediente_repo)
