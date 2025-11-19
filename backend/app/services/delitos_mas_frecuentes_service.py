from typing import Generator
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.delitos_mas_frecuentes_schema import (
    DelitosMasFrecuentesResponse,
    DatosGraficoDelitosMasFrecuentes,
    DelitoItem
)


class DelitosMasFrecuentesService:
    """
    Service para el gráfico de delitos más frecuentes.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_grafico(self, limit: int = 10) -> DelitosMasFrecuentesResponse:
        """
        Obtiene datos de delitos más frecuentes listos para graficar.
        
        Args:
            limit: Número máximo de delitos a retornar (default: 10)
            
        Returns:
            DelitosMasFrecuentesResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de delitos
        - data: Lista de cantidad de causas por delito
        - delitos: Lista completa con todos los datos de cada delito
        - total_causas: Total de causas en todos los delitos
        """
        # Obtener datos del repository
        delitos_data = self.expediente_repository.get_delitos_mas_frecuentes(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        cantidades = []
        delitos_items = []
        
        # Calcular total
        total_causas = sum(item['cantidad_causas'] for item in delitos_data)
        
        for i, delito_data in enumerate(delitos_data):
            labels.append(delito_data['delito'])
            cantidades.append(delito_data['cantidad_causas'])
            
            # Crear item completo
            delitos_items.append(DelitoItem(
                delito=delito_data['delito'],
                cantidad_causas=delito_data['cantidad_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoDelitosMasFrecuentes(
            labels=labels,
            data=cantidades,
            delitos=delitos_items,
            total_causas=total_causas
        )
        
        return DelitosMasFrecuentesResponse(datos_grafico=datos_grafico)


def get_delitos_mas_frecuentes_service(
    expediente_repo: ExpedienteRepository
) -> Generator[DelitosMasFrecuentesService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del DelitosMasFrecuentesService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de DelitosMasFrecuentesService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/delitos-mas-frecuentes")
        def get_delitos(
            service: DelitosMasFrecuentesService = Depends(get_delitos_mas_frecuentes_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield DelitosMasFrecuentesService(expediente_repo)

