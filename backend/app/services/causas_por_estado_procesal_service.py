from typing import Generator
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.expedientes_por_estado_procesal_schema import (
    CasosPorEstadoProcesalResponse,
    DatosGraficoEstadoProcesal
)


class CausasPorEstadoProcesalService:
    """
    Service para el gráfico de causas por estado procesal.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_grafico(self) -> CasosPorEstadoProcesalResponse:
        """
        Obtiene datos agregados por estado procesal listos para graficar.
        
        Returns:
            CasosPorEstadoProcesalResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de estados procesales
        - data: Lista de conteos por estado
        - porcentajes: Lista de porcentajes por estado
        - total: Total de casos
        """
        # Estados procesales válidos
        estados = ['En trámite', 'Terminada']
        
        # Obtener conteos por estado
        conteos = []
        for estado in estados:
            count = self.expediente_repository.count_by_estado_procesal(estado)
            conteos.append(count)
        
        # Calcular total
        total = sum(conteos)
        
        # Calcular porcentajes
        porcentajes = []
        if total > 0:
            porcentajes = [(count / total * 100) for count in conteos]
        else:
            porcentajes = [0.0, 0.0]
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoEstadoProcesal(
            labels=estados,
            data=conteos,
            porcentajes=porcentajes,
            total=total
        )
        
        return CasosPorEstadoProcesalResponse(datos_grafico=datos_grafico)


def get_causas_por_estado_procesal_service(
    expediente_repo: ExpedienteRepository
) -> Generator[CausasPorEstadoProcesalService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del CausasPorEstadoProcesalService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de CausasPorEstadoProcesalService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/casos-por-estado")
        def get_casos(
            service: CausasPorEstadoProcesalService = Depends(get_causas_por_estado_procesal_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield CausasPorEstadoProcesalService(expediente_repo)
