from typing import Generator
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.causas_por_fiscal_schema import (
    CausasPorFiscalResponse,
    DatosGraficoCausasPorFiscal,
    FiscalCausasItem
)
from app.utils.text_formatter import formatear_texto


class CausasPorFiscalService:
    """
    Service para el gráfico de causas por fiscal clasificadas por abiertas y terminadas.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_grafico(self, limit: int = 20) -> CausasPorFiscalResponse:
        """
        Obtiene datos agregados de causas por fiscal listos para graficar.
        
        Args:
            limit: Número máximo de fiscales a retornar (default: 20)
            
        Returns:
            CausasPorFiscalResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de fiscales
        - causas_abiertas: Lista de cantidad de causas abiertas por fiscal
        - causas_terminadas: Lista de cantidad de causas terminadas por fiscal
        - fiscales: Lista de objetos con fiscal y cantidades
        - totales: Totales generales de causas abiertas, terminadas y total
        """
        # Obtener datos del repository
        fiscales_data = self.expediente_repository.get_causas_por_fiscal(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        causas_abiertas = []
        causas_terminadas = []
        fiscales_items = []
        
        # Calcular totales
        total_causas_abiertas = sum(item['causas_abiertas'] for item in fiscales_data)
        total_causas_terminadas = sum(item['causas_terminadas'] for item in fiscales_data)
        total_causas = sum(item['total_causas'] for item in fiscales_data)
        
        for item in fiscales_data:
            # Formatear el nombre del fiscal
            fiscal_formateado = formatear_texto(item['fiscal'])
            
            labels.append(fiscal_formateado)
            causas_abiertas.append(item['causas_abiertas'])
            causas_terminadas.append(item['causas_terminadas'])
            
            # Crear item completo
            fiscales_items.append(FiscalCausasItem(
                fiscal=fiscal_formateado,
                causas_abiertas=item['causas_abiertas'],
                causas_terminadas=item['causas_terminadas'],
                total_causas=item['total_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoCausasPorFiscal(
            labels=labels,
            causas_abiertas=causas_abiertas,
            causas_terminadas=causas_terminadas,
            fiscales=fiscales_items,
            total_causas_abiertas=total_causas_abiertas,
            total_causas_terminadas=total_causas_terminadas,
            total_causas=total_causas
        )
        
        return CausasPorFiscalResponse(datos_grafico=datos_grafico)


def get_causas_por_fiscal_service(
    expediente_repo: ExpedienteRepository
) -> Generator[CausasPorFiscalService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del CausasPorFiscalService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de CausasPorFiscalService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/causas-por-fiscal")
        def get_causas(
            service: CausasPorFiscalService = Depends(get_causas_por_fiscal_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield CausasPorFiscalService(expediente_repo)

