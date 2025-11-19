from typing import Generator
from app.repositories.juez_repository import JuezRepository
from app.schemas.jueces_mayor_demora_schema import (
    JuecesMayorDemoraResponse,
    DatosGraficoJuecesMayorDemora,
    JuezDemoraItem
)
from app.utils.text_formatter import formatear_texto


class JuecesMayorDemoraService:
    """
    Service para el gráfico de jueces con mayor demora.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, juez_repository: JuezRepository):
        """
        Inicializa el service con el repository de jueces.
        
        Args:
            juez_repository: Instancia del JuezRepository
        """
        self.juez_repository = juez_repository
    
    def get_datos_grafico(self, limit: int = 10) -> JuecesMayorDemoraResponse:
        """
        Obtiene datos de jueces con mayor demora listos para graficar.
        
        Args:
            limit: Número máximo de jueces a retornar (default: 10)
            
        Returns:
            JuecesMayorDemoraResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de labels (Juez - Tribunal)
        - data: Lista de demoras promedio en días
        - cantidad_expedientes: Lista de cantidad de expedientes
        - jueces: Lista completa con todos los datos
        """
        # Obtener datos del repository
        jueces_data = self.juez_repository.get_jueces_con_mayor_demora(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        demoras = []
        cantidades = []
        jueces_items = []
        
        for juez_data in jueces_data:
            # Formatear nombres de juez y tribunal
            juez_formateado = formatear_texto(juez_data['juez_nombre'])
            tribunal_formateado = formatear_texto(juez_data['tribunal_nombre'])
            
            # Crear label combinando juez y tribunal
            label = f"{juez_formateado} - {tribunal_formateado}"
            labels.append(label)
            
            demoras.append(juez_data['demora_promedio_dias'])
            cantidades.append(juez_data['cantidad_expedientes'])
            
            # Crear item completo
            jueces_items.append(JuezDemoraItem(
                juez_nombre=juez_formateado,
                tribunal_nombre=tribunal_formateado,
                demora_promedio_dias=juez_data['demora_promedio_dias'],
                cantidad_expedientes=juez_data['cantidad_expedientes'],
                label=label
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoJuecesMayorDemora(
            labels=labels,
            data=demoras,
            cantidad_expedientes=cantidades,
            jueces=jueces_items
        )
        
        return JuecesMayorDemoraResponse(datos_grafico=datos_grafico)


def get_jueces_mayor_demora_service(
    juez_repo: JuezRepository
) -> Generator[JuecesMayorDemoraService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del JuecesMayorDemoraService.
    El JuezRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de JuecesMayorDemoraService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/jueces-mayor-demora")
        def get_jueces(
            service: JuecesMayorDemoraService = Depends(get_jueces_mayor_demora_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el JuezRepository
    usando get_juez_repository() como sub-dependency.
    """
    yield JuecesMayorDemoraService(juez_repo)

