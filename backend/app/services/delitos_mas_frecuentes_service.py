import re
from typing import Generator
from app.repositories.expediente_repository import ExpedienteRepository
from app.schemas.delitos_mas_frecuentes_schema import (
    DelitosMasFrecuentesResponse,
    DatosGraficoDelitosMasFrecuentes,
    DelitoItem
)
from app.utils.text_formatter import formatear_texto


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
    
    def _limpiar_nombre_delito(self, nombre: str) -> str:
        """
        Limpia el nombre del delito eliminando paréntesis y su contenido.
        Maneja tanto paréntesis cerrados como sin cerrar.
        
        Args:
            nombre: Nombre del delito con posibles paréntesis
            
        Returns:
            Nombre del delito sin paréntesis ni su contenido
        """
        nombre_limpio = re.sub(r'\([^)]*\)', '', nombre)
        nombre_limpio = re.sub(r'\([^)]*$', '', nombre_limpio)
        nombre_limpio = ' '.join(nombre_limpio.split())
        return nombre_limpio.strip()
    
    def get_datos_grafico(self, limit: int = 10) -> DelitosMasFrecuentesResponse:
        """
        Obtiene datos de delitos más frecuentes listos para graficar, separados por estado.
        
        Args:
            limit: Número máximo de delitos a retornar (default: 10)
            
        Returns:
            DelitosMasFrecuentesResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de delitos
        - causas_abiertas: Lista de cantidad de causas abiertas por delito
        - causas_terminadas: Lista de cantidad de causas terminadas por delito
        - data: Lista de cantidad total de causas por delito (para compatibilidad)
        - delitos: Lista completa con todos los datos de cada delito
        - totales: Totales de causas abiertas, terminadas y total
        """
        # Obtener datos del repository
        delitos_data = self.expediente_repository.get_delitos_mas_frecuentes(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        causas_abiertas = []
        causas_terminadas = []
        cantidades = []
        delitos_items = []
        
        # Calcular totales
        total_causas_abiertas = sum(item['cantidad_causas_abiertas'] for item in delitos_data)
        total_causas_terminadas = sum(item['cantidad_causas_terminadas'] for item in delitos_data)
        total_causas = sum(item['cantidad_causas'] for item in delitos_data)
        
        for i, delito_data in enumerate(delitos_data):
            # Limpiar el nombre del delito eliminando paréntesis y su contenido
            nombre_limpio = self._limpiar_nombre_delito(delito_data['delito'])
            # Formatear el texto (Title Case, excepto siglas)
            nombre_formateado = formatear_texto(nombre_limpio)
            
            labels.append(nombre_formateado)
            causas_abiertas.append(delito_data['cantidad_causas_abiertas'])
            causas_terminadas.append(delito_data['cantidad_causas_terminadas'])
            cantidades.append(delito_data['cantidad_causas'])
            
            # Crear item completo con el nombre formateado
            delitos_items.append(DelitoItem(
                delito=nombre_formateado,
                cantidad_causas_abiertas=delito_data['cantidad_causas_abiertas'],
                cantidad_causas_terminadas=delito_data['cantidad_causas_terminadas'],
                cantidad_causas=delito_data['cantidad_causas']
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoDelitosMasFrecuentes(
            labels=labels,
            causas_abiertas=causas_abiertas,
            causas_terminadas=causas_terminadas,
            data=cantidades,
            delitos=delitos_items,
            total_causas_abiertas=total_causas_abiertas,
            total_causas_terminadas=total_causas_terminadas,
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

