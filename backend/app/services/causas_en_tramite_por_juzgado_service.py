from typing import Generator, List
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.causas_en_tramite_por_juzgado_schema import (
    CausasEnTramitePorJuzgadoResponse,
    DatosGraficoCausasEnTramitePorJuzgado,
    JuzgadoCausasItem
)


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
        Obtiene datos agregados de causas en trámite por juzgado listos para graficar.
        
        Args:
            limit: Número máximo de juzgados a retornar (default: 20)
            
        Returns:
            CausasEnTramitePorJuzgadoResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de juzgados/tribunales
        - data: Lista de cantidad de causas en trámite por juzgado
        - juzgados: Lista de objetos con tribunal y cantidad
        - total_causas_en_tramite: Total general de causas en trámite
        """
        # Obtener datos del repository
        juzgados_data = self.expediente_repository.get_causas_en_tramite_por_juzgado(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        data = []
        juzgados_items = []
        
        # Calcular total
        total_causas_en_tramite = sum(item['cantidad_causas_en_tramite'] for item in juzgados_data)
        
        for item in juzgados_data:
            labels.append(item['tribunal'])
            data.append(item['cantidad_causas_en_tramite'])
            
            # Crear item completo
            juzgados_items.append(JuzgadoCausasItem(
                tribunal=item['tribunal'],
                cantidad_causas_en_tramite=item['cantidad_causas_en_tramite']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoCausasEnTramitePorJuzgado(
            labels=labels,
            data=data,
            juzgados=juzgados_items,
            total_causas_en_tramite=total_causas_en_tramite
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

