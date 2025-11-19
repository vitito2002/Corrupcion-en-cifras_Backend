from typing import Generator
from app.repositories.parte_repository import ParteRepository
from app.schemas.personas_mas_denunciadas_schema import (
    PersonasMasDenunciadasResponse,
    DatosGraficoPersonasMasDenunciadas,
    PersonaDenunciadaItem
)
from app.utils.text_formatter import formatear_texto


class PersonasMasDenunciadasService:
    """
    Service para el gráfico de personas más denunciadas.
    Procesa datos del repository y los prepara listos para graficar.
    """
    
    def __init__(self, parte_repository: ParteRepository):
        """
        Inicializa el service con el repository de partes.
        
        Args:
            parte_repository: Instancia del ParteRepository
        """
        self.parte_repository = parte_repository
    
    def get_datos_grafico(self, limit: int = 20) -> PersonasMasDenunciadasResponse:
        """
        Obtiene datos agregados de personas más denunciadas listos para graficar.
        
        Args:
            limit: Número máximo de personas a retornar (default: 20)
            
        Returns:
            PersonasMasDenunciadasResponse con datos procesados listos para el frontend
            
        El formato de respuesta incluye:
        - labels: Lista de nombres de personas
        - data: Lista de cantidad de causas por persona
        - personas: Lista de objetos con persona y cantidad
        - total_causas: Total general de causas
        """
        # Obtener datos del repository
        personas_data = self.parte_repository.get_personas_mas_denunciadas(limit=limit)
        
        # Procesar datos para el gráfico
        labels = []
        data = []
        personas_items = []
        
        # Calcular total
        total_causas = sum(item['cantidad_causas'] for item in personas_data)
        
        for item in personas_data:
            # Filtrar valores null, None o vacíos
            if not item.get('persona') or not item.get('cantidad_causas'):
                continue
            
            # Formatear el nombre de la persona
            persona_formateada = formatear_texto(item['persona'])
            
            # Validar que el nombre formateado no esté vacío
            if not persona_formateada or persona_formateada.strip() == '':
                continue
            
            # Validar que cantidad_causas sea un número válido
            cantidad = item['cantidad_causas']
            if not isinstance(cantidad, (int, float)) or cantidad <= 0:
                continue
            
            labels.append(persona_formateada)
            data.append(int(cantidad))
            
            # Crear item completo
            personas_items.append(PersonaDenunciadaItem(
                persona=persona_formateada,
                cantidad_causas=int(cantidad)
            ))
        
        # Preparar datos del gráfico
        datos_grafico = DatosGraficoPersonasMasDenunciadas(
            labels=labels,
            data=data,
            personas=personas_items,
            total_causas=total_causas
        )
        
        return PersonasMasDenunciadasResponse(datos_grafico=datos_grafico)


def get_personas_mas_denunciadas_service(
    parte_repo: ParteRepository
) -> Generator[PersonasMasDenunciadasService, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del PersonasMasDenunciadasService.
    El ParteRepository se inyecta automáticamente como sub-dependency.
    
    Yields:
        Instancia de PersonasMasDenunciadasService
        
    Usage en FastAPI:
        from fastapi import Depends
        
        @app.get("/analytics/personas-mas-denunciadas")
        def get_personas(
            service: PersonasMasDenunciadasService = Depends(get_personas_mas_denunciadas_service)
        ):
            return service.get_datos_grafico()
            
    Nota: FastAPI inyectará automáticamente el ParteRepository
    usando get_parte_repository() como sub-dependency.
    """
    yield PersonasMasDenunciadasService(parte_repo)

