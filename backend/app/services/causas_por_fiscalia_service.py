from typing import Generator
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.causas_por_fiscalia_schema import (
    CausasPorFiscaliaResponse,
    DatosGraficoCausasPorFiscalia,
    FiscaliaCausasItem
)
from app.utils.text_formatter import formatear_texto


class CausasPorFiscaliaService:
    """
    Service para el gráfico de causas por fiscalía clasificadas por abiertas y terminadas.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_grafico(self, limit: int = 20) -> CausasPorFiscaliaResponse:
        """
        Obtiene datos agregados de causas por fiscalía listos para graficar.
        
        Args:
            limit: Número máximo de fiscalías a retornar (default: 20)
            
        Returns:
            CausasPorFiscaliaResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de fiscalías
        - causas_abiertas: Lista de cantidad de causas abiertas por fiscalía
        - causas_terminadas: Lista de cantidad de causas terminadas por fiscalía
        - fiscalias: Lista de objetos con fiscalía y cantidades
        - totales: Totales generales de causas abiertas, terminadas y total
        """
        # Obtener datos del repository
        fiscalias_data = self.expediente_repository.get_causas_por_fiscalia(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        causas_abiertas = []
        causas_terminadas = []
        fiscalias_items = []
        
        # Calcular totales
        total_causas_abiertas = sum(item['causas_abiertas'] for item in fiscalias_data)
        total_causas_terminadas = sum(item['causas_terminadas'] for item in fiscalias_data)
        total_causas = sum(item['total_causas'] for item in fiscalias_data)
        
        for item in fiscalias_data:
            # Formatear el nombre de la fiscalía
            fiscalia_formateada = formatear_texto(item['fiscalia'])
            
            labels.append(fiscalia_formateada)
            causas_abiertas.append(item['causas_abiertas'])
            causas_terminadas.append(item['causas_terminadas'])
            
            # Crear item completo
            fiscalias_items.append(FiscaliaCausasItem(
                fiscalia=fiscalia_formateada,
                causas_abiertas=item['causas_abiertas'],
                causas_terminadas=item['causas_terminadas'],
                total_causas=item['total_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoCausasPorFiscalia(
            labels=labels,
            causas_abiertas=causas_abiertas,
            causas_terminadas=causas_terminadas,
            fiscalias=fiscalias_items,
            total_causas_abiertas=total_causas_abiertas,
            total_causas_terminadas=total_causas_terminadas,
            total_causas=total_causas
        )
        
        return CausasPorFiscaliaResponse(datos_grafico=datos_grafico)


def get_causas_por_fiscalia_service(
    expediente_repo: ExpedienteRepository
) -> Generator[CausasPorFiscaliaService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del CausasPorFiscaliaService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de CausasPorFiscaliaService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/causas-por-fiscal")
        def get_causas(
            service: CausasPorFiscaliaService = Depends(get_causas_por_fiscalia_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield CausasPorFiscaliaService(expediente_repo)

