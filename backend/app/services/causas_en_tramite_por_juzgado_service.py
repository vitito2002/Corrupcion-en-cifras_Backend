from typing import Generator, List
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.causas_en_tramite_por_juzgado_schema import (
    CausasEnTramitePorJuzgadoResponse,
    DatosGraficoCausasEnTramitePorJuzgado,
    JuzgadoCausasItem
)
from app.utils.text_formatter import formatear_texto


class CausasEnTramitePorJuzgadoService:
    """
    Service para el gráfico de causas en trámite por juzgado.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_grafico(self, limit: int = 20) -> CausasEnTramitePorJuzgadoResponse:
        """
        Obtiene datos agregados de causas por juzgado listos para graficar, separadas por estado.
        
        Args:
            limit: Número máximo de juzgados a retornar (default: 20)
            
        Returns:
            CausasEnTramitePorJuzgadoResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de juzgados/tribunales
        - causas_abiertas: Lista de cantidad de causas en trámite por juzgado
        - causas_terminadas: Lista de cantidad de causas terminadas por juzgado
        - data: Lista de cantidad total de causas por juzgado (para compatibilidad)
        - juzgados: Lista de objetos con tribunal y cantidades
        - totales: Totales generales de causas abiertas, terminadas y total
        """
        # Obtener datos del repository
        juzgados_data = self.expediente_repository.get_causas_por_juzgado(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        causas_abiertas = []
        causas_terminadas = []
        data = []
        juzgados_items = []
        
        # Calcular totales
        total_causas_abiertas = sum(item['cantidad_causas_abiertas'] for item in juzgados_data)
        total_causas_terminadas = sum(item['cantidad_causas_terminadas'] for item in juzgados_data)
        total_causas = sum(item['cantidad_causas'] for item in juzgados_data)
        
        for item in juzgados_data:
            # Formatear el nombre del tribunal
            tribunal_formateado = formatear_texto(item['tribunal'])
            
            labels.append(tribunal_formateado)
            causas_abiertas.append(item['cantidad_causas_abiertas'])
            causas_terminadas.append(item['cantidad_causas_terminadas'])
            data.append(item['cantidad_causas'])
            
            # Crear item completo
            juzgados_items.append(JuzgadoCausasItem(
                tribunal=tribunal_formateado,
                cantidad_causas_abiertas=item['cantidad_causas_abiertas'],
                cantidad_causas_terminadas=item['cantidad_causas_terminadas'],
                cantidad_causas=item['cantidad_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoCausasEnTramitePorJuzgado(
            labels=labels,
            causas_abiertas=causas_abiertas,
            causas_terminadas=causas_terminadas,
            data=data,
            juzgados=juzgados_items,
            total_causas_abiertas=total_causas_abiertas,
            total_causas_terminadas=total_causas_terminadas,
            total_causas_en_tramite=total_causas_abiertas,  # Para compatibilidad
            total_causas=total_causas
        )
        
        return CausasEnTramitePorJuzgadoResponse(datos_grafico=datos_grafico)


def get_causas_en_tramite_por_juzgado_service(
    expediente_repo: ExpedienteRepository
) -> Generator[CausasEnTramitePorJuzgadoService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del CausasEnTramitePorJuzgadoService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de CausasEnTramitePorJuzgadoService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/causas-en-tramite-por-juzgado")
        def get_causas(
            service: CausasEnTramitePorJuzgadoService = Depends(get_causas_en_tramite_por_juzgado_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield CausasEnTramitePorJuzgadoService(expediente_repo)

