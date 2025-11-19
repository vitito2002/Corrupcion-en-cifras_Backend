from typing import Generator, List
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.causas_por_fuero_schema import (
    CausasPorFueroResponse,
    DatosGraficoCausasPorFuero,
    FueroCausaItem
)
from app.utils.text_formatter import formatear_texto


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
        Obtiene datos agregados de causas por fuero listos para graficar, separadas por estado.
        
        Returns:
            CausasPorFueroResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de fueros
        - causas_abiertas: Lista de cantidad de causas abiertas por fuero
        - causas_terminadas: Lista de cantidad de causas terminadas por fuero
        - data: Lista de cantidad total de causas por fuero (para compatibilidad)
        - fueros: Lista de objetos con fuero y cantidades
        - totales: Totales generales de causas abiertas, terminadas y total
        """
        # Obtener datos del repository
        fueros_data = self.expediente_repository.get_causas_por_fuero()
        
        # Procesar datos para el gráfico
        labels = []
        causas_abiertas = []
        causas_terminadas = []
        data = []
        fueros_items = []
        
        # Calcular totales
        total_causas_abiertas = sum(item['cantidad_causas_abiertas'] for item in fueros_data)
        total_causas_terminadas = sum(item['cantidad_causas_terminadas'] for item in fueros_data)
        total_causas = sum(item['cantidad_causas'] for item in fueros_data)
        
        for item in fueros_data:
            # Formatear el nombre del fuero
            fuero_formateado = formatear_texto(item['fuero'])
            
            labels.append(fuero_formateado)
            causas_abiertas.append(item['cantidad_causas_abiertas'])
            causas_terminadas.append(item['cantidad_causas_terminadas'])
            data.append(item['cantidad_causas'])
            
            # Crear item completo
            fueros_items.append(FueroCausaItem(
                fuero=fuero_formateado,
                cantidad_causas_abiertas=item['cantidad_causas_abiertas'],
                cantidad_causas_terminadas=item['cantidad_causas_terminadas'],
                cantidad_causas=item['cantidad_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoCausasPorFuero(
            labels=labels,
            causas_abiertas=causas_abiertas,
            causas_terminadas=causas_terminadas,
            data=data,
            fueros=fueros_items,
            total_causas_abiertas=total_causas_abiertas,
            total_causas_terminadas=total_causas_terminadas,
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

