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
        # Obtener datos del repository
        causas_data = self.expediente_repository.get_duracion_instruccion(limit=limit)
        
        if not causas_data:
            # Si no hay datos, retornar estructura vacía
            return DuracionInstruccionResponse(
                datos_grafico=DatosGraficoDuracionInstruccion(
                    labels=[],
                    data=[],
                    causas=[],
                    duracion_promedio_dias=0.0,
                    duracion_maxima_dias=0,
                    duracion_minima_dias=0,
                    total_causas=0
                )
            )
        
        # Procesar datos para el gráfico
        labels = []
        duraciones = []
        causas_items = []
        
        # Calcular estadísticas
        duraciones_list = [causa['duracion_dias'] for causa in causas_data]
        duracion_promedio = sum(duraciones_list) / len(duraciones_list) if duraciones_list else 0.0
        duracion_maxima = max(duraciones_list) if duraciones_list else 0
        duracion_minima = min(duraciones_list) if duraciones_list else 0
        
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
        datos_grafico = DatosGraficoDuracionInstruccion(
            labels=labels,
            data=duraciones,
            causas=causas_items,
            duracion_promedio_dias=round(duracion_promedio, 2),
            duracion_maxima_dias=duracion_maxima,
            duracion_minima_dias=duracion_minima,
            total_causas=len(causas_data)
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

