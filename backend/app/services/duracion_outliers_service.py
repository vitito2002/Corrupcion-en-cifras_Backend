from typing import Generator
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.duracion_outliers_schema import (
    DuracionOutliersResponse,
    DatosGraficoDuracionOutliers,
    CausaOutlierItem
)


class DuracionOutliersService:
    """
    Service para el análisis de outliers de duración de instrucción.
    Procesa datos del repository y los prepara listos para mostrar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_outliers(self, limit: int = 5) -> DuracionOutliersResponse:
        """
        Obtiene los outliers de duración de instrucción (top más largos y top más cortos).
        
        Args:
            limit: Número máximo de causas a retornar en cada categoría (default: 5)
            
        Returns:
            DuracionOutliersResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - causas_mas_largas: Top causas con mayor duración
        - causas_mas_cortas: Top causas con menor duración
        """
        # Obtener datos del repository
        causas_mas_largas_data = self.expediente_repository.get_duracion_outliers_mas_largos(limit=limit)
        causas_mas_cortas_data = self.expediente_repository.get_duracion_outliers_mas_cortos(limit=limit)
        
        # Procesar causas más largas
        causas_mas_largas_items = []
        for causa in causas_mas_largas_data:
            causas_mas_largas_items.append(CausaOutlierItem(
                numero_expediente=causa['numero_expediente'],
                caratula=causa['caratula'],
                tribunal=causa['tribunal'],
                estado_procesal=causa['estado_procesal'],
                fecha_inicio=causa['fecha_inicio'],
                fecha_ultimo_movimiento=causa['fecha_ultimo_movimiento'],
                duracion_dias=causa['duracion_dias'],
                imputado_nombre=causa.get('imputado_nombre')
            ))
        
        # Procesar causas más cortas
        causas_mas_cortas_items = []
        for causa in causas_mas_cortas_data:
            causas_mas_cortas_items.append(CausaOutlierItem(
                numero_expediente=causa['numero_expediente'],
                caratula=causa['caratula'],
                tribunal=causa['tribunal'],
                estado_procesal=causa['estado_procesal'],
                fecha_inicio=causa['fecha_inicio'],
                fecha_ultimo_movimiento=causa['fecha_ultimo_movimiento'],
                duracion_dias=causa['duracion_dias'],
                imputado_nombre=causa.get('imputado_nombre')
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoDuracionOutliers(
            causas_mas_largas=causas_mas_largas_items,
            causas_mas_cortas=causas_mas_cortas_items
        )
        
        return DuracionOutliersResponse(datos_grafico=datos_grafico)


def get_duracion_outliers_service(
    expediente_repo: ExpedienteRepository
) -> Generator[DuracionOutliersService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del DuracionOutliersService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de DuracionOutliersService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/duracion-outliers")
        def get_outliers(
            service: DuracionOutliersService = Depends(get_duracion_outliers_service)
        ):
            return service.get_datos_outliers()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield DuracionOutliersService(expediente_repo)

