from typing import Generator
import math
from app.repositories.parte_repository import ParteRepository
from app.schemas.personas_que_mas_denunciaron_schema import (
    PersonasQueMasDenunciaronResponse,
    DatosGraficoPersonasQueMasDenunciaron,
    PersonaDenuncianteItem
)
from app.utils.text_formatter import formatear_texto


class PersonasQueMasDenunciaronService:
    """
    Service para el gráfico de personas que más denunciaron.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, parte_repository: ParteRepository):
        """
        Inicializa el service con el repository de partes.
        
        Args:
            parte_repository: Instancia del ParteRepository
        """
        self.parte_repository = parte_repository
    
    def get_datos_grafico(self, limit: int = 20) -> PersonasQueMasDenunciaronResponse:
        """
        Obtiene datos agregados de personas que más denunciaron listos para graficar.
        
        Args:
            limit: Número máximo de personas a retornar (default: 20)
            
        Returns:
            PersonasQueMasDenunciaronResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de personas
        - data: Lista de cantidad de denuncias por persona
        - personas: Lista de objetos con persona y cantidad
        - total_denuncias: Total general de denuncias
        """
        # Obtener datos del repository
        personas_data = self.parte_repository.get_personas_que_mas_denunciaron(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        data = []
        personas_items = []
        
        # Calcular total
        total_denuncias = sum(item['cantidad_denuncias'] for item in personas_data)
        
        for item in personas_data:
            # Filtrar valores null, None o vacíos
            if not item.get('persona') or not item.get('cantidad_denuncias'):
                continue
            
            # Filtrar si el nombre es "NaN" (como string)
            persona_raw = str(item['persona']).strip().upper()
            if persona_raw == 'NAN' or persona_raw == 'N/A':
                continue
            
            # Validar que cantidad_denuncias sea un número válido y no sea NaN
            cantidad = item['cantidad_denuncias']
            if not isinstance(cantidad, (int, float)):
                continue
            
            # Filtrar NaN explícitamente
            if isinstance(cantidad, float) and math.isnan(cantidad):
                continue
            
            # Filtrar valores <= 0
            if cantidad <= 0:
                continue
            
            # Formatear el nombre de la persona
            persona_formateada = formatear_texto(item['persona'])
            
            # Validar que el nombre formateado no esté vacío y no sea "NaN"
            if not persona_formateada or persona_formateada.strip() == '':
                continue
            
            # Filtrar si después de formatear sigue siendo "NaN"
            if persona_formateada.strip().upper() == 'NAN':
                continue
            
            labels.append(persona_formateada)
            data.append(int(cantidad))
            
            # Crear item completo
            personas_items.append(PersonaDenuncianteItem(
                persona=persona_formateada,
                cantidad_denuncias=int(cantidad)
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoPersonasQueMasDenunciaron(
            labels=labels,
            data=data,
            personas=personas_items,
            total_denuncias=total_denuncias
        )
        
        return PersonasQueMasDenunciaronResponse(datos_grafico=datos_grafico)


def get_personas_que_mas_denunciaron_service(
    parte_repo: ParteRepository
) -> Generator[PersonasQueMasDenunciaronService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del PersonasQueMasDenunciaronService.
    El ParteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de PersonasQueMasDenunciaronService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/personas-que-mas-denunciaron")
        def get_personas(
            service: PersonasQueMasDenunciaronService = Depends(get_personas_que_mas_denunciaron_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ParteRepository
    usando get_parte_repository() como sub-dependency.
    """
    yield PersonasQueMasDenunciaronService(parte_repo)

