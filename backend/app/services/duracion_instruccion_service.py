from typing import Generator, List
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.duracion_instruccion_schema import (
    DuracionInstruccionResponse,
    DatosGraficoDuracionInstruccion,
    CausaDuracionItem
)


class DuracionInstruccionService:
    """
    Service para el gráfico de duración de instrucción.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, expediente_repository: ExpedienteRepository):
        """
        Inicializa el service con el repository de expedientes.
        
        Args:
            expediente_repository: Instancia del ExpedienteRepository
        """
        self.expediente_repository = expediente_repository
    
    def get_datos_grafico(self, limit: int = 50) -> DuracionInstruccionResponse:
        """
        Obtiene datos agregados de duración de instrucción listos para graficar.
        
        Args:
            limit: Número máximo de causas a retornar (default: 50)
            
        Returns:
            DuracionInstruccionResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de números de expediente o carátulas
        - data: Lista de duración en días
        - causas: Lista completa de causas con todos los datos
        - duracion_promedio_dias: Duración promedio en días
        - duracion_maxima_dias: Duración máxima en días
        - duracion_minima_dias: Duración mínima en días
        - total_causas: Total de causas analizadas
        """
        # Obtener estadísticas globales (de TODAS las causas, no solo las limitadas)
        estadisticas_globales = self.expediente_repository.get_duracion_promedio_global()
        
        # Obtener datos del repository para el gráfico (limitadas por limit)
        causas_data = self.expediente_repository.get_duracion_instruccion(limit=limit)
        
        if not causas_data:
            # Si no hay datos, retornar estructura vacía
            return DuracionInstruccionResponse(
                datos_grafico=DatosGraficoDuracionInstruccion(
                    labels=[],
                    data=[],
                    causas=[],
                    duracion_promedio_dias=estadisticas_globales["duracion_promedio_dias"],
                    duracion_maxima_dias=estadisticas_globales["duracion_maxima_dias"],
                    duracion_minima_dias=estadisticas_globales["duracion_minima_dias"],
                    total_causas=estadisticas_globales["total_causas"]
                )
            )
        
        # Procesar datos para el gráfico
        labels = []
        duraciones = []
        causas_items = []
        
        for causa in causas_data:
            # Usar carátula si está disponible, sino número de expediente
            label = causa['caratula'] if causa['caratula'] else causa['numero_expediente']
            # Truncar label si es muy largo
            if len(label) > 60:
                label = label[:57] + "..."
            
            labels.append(label)
            duraciones.append(causa['duracion_dias'])
            
            # Crear item completo
            causas_items.append(CausaDuracionItem(
                numero_expediente=causa['numero_expediente'],
                caratula=causa['caratula'],
                tribunal=causa['tribunal'],
                estado_procesal=causa['estado_procesal'],
                fecha_inicio=causa['fecha_inicio'],
                fecha_ultimo_movimiento=causa['fecha_ultimo_movimiento'],
                duracion_dias=causa['duracion_dias']
            ))
        
        # Preparar datos del gráfico
        # Usar estadísticas globales para el promedio, máximo y mínimo
        # El total_causas es el total de todas las causas analizadas, no solo las limitadas
        datos_grafico = DatosGraficoDuracionInstruccion(
            labels=labels,
            data=duraciones,
            causas=causas_items,
            duracion_promedio_dias=round(estadisticas_globales["duracion_promedio_dias"], 2),
            duracion_maxima_dias=estadisticas_globales["duracion_maxima_dias"],
            duracion_minima_dias=estadisticas_globales["duracion_minima_dias"],
            total_causas=estadisticas_globales["total_causas"]
        )
        
        return DuracionInstruccionResponse(datos_grafico=datos_grafico)


def get_duracion_instruccion_service(
    expediente_repo: ExpedienteRepository
) -> Generator[DuracionInstruccionService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del DuracionInstruccionService.
    El ExpedienteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de DuracionInstruccionService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/duracion-instruccion")
        def get_duracion(
            service: DuracionInstruccionService = Depends(get_duracion_instruccion_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ExpedienteRepository
    usando get_expediente_repository() como sub-dependency.
    """
    yield DuracionInstruccionService(expediente_repo)

