from typing import Generator
from app.repositories.juez_repository import JuezRepository
from app.schemas.jueces_mayor_demora_schema import (
    JuecesMayorDemoraResponse,
    DatosGraficoJuecesMayorDemora,
    JuezDemoraItem
)


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
        - colores: Colores generados automáticamente para el gráfico
        """
        # Obtener datos del repository
        jueces_data = self.juez_repository.get_jueces_con_mayor_demora(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        demoras = []
        cantidades = []
        jueces_items = []
        
        # Generar colores (gradiente de rojo a amarillo para mayor demora)
        colores = self._generar_colores(len(jueces_data))
        
        for juez_data in jueces_data:
            # Crear label combinando juez y tribunal
            label = f"{juez_data['juez_nombre']} - {juez_data['tribunal_nombre']}"
            labels.append(label)
            
            demoras.append(juez_data['demora_promedio_dias'])
            cantidades.append(juez_data['cantidad_expedientes'])
            
            # Crear item completo
            jueces_items.append(JuezDemoraItem(
                juez_nombre=juez_data['juez_nombre'],
                tribunal_nombre=juez_data['tribunal_nombre'],
                demora_promedio_dias=juez_data['demora_promedio_dias'],
                cantidad_expedientes=juez_data['cantidad_expedientes'],
                label=label
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoJuecesMayorDemora(
            labels=labels,
            data=demoras,
            cantidad_expedientes=cantidades,
            jueces=jueces_items,
            colores=colores
        )
        
        return JuecesMayorDemoraResponse(datos_grafico=datos_grafico)
    
    def _generar_colores(self, cantidad: int) -> list[str]:
        """
        Genera colores en gradiente de rojo (mayor demora) a amarillo (menor demora).
        
        Args:
            cantidad: Número de colores a generar
            
        Returns:
            Lista de colores en formato hexadecimal
        """
        if cantidad == 0:
            return []
        
        colores = []
        # Gradiente de rojo (#FF0000) a amarillo (#FFD700) pasando por naranja
        for i in range(cantidad):
            # Interpolación: más rojo al inicio, más amarillo al final
            ratio = i / max(cantidad - 1, 1)
            
            # Rojo a naranja a amarillo
            if ratio < 0.5:
                # Rojo a naranja
                r = 255
                g = int(128 * ratio * 2)
                b = 0
            else:
                # Naranja a amarillo
                r = 255
                g = int(128 + (127 * (ratio - 0.5) * 2))
                b = 0
            
            color = f"#{r:02X}{g:02X}{b:02X}"
            colores.append(color)
        
        return colores


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

