from typing import Generator
from app.repositories.parte_repository import ParteRepository
from app.schemas.personas_que_mas_denunciaron_schema import (
    PersonasQueMasDenunciaronResponse,
    DatosGraficoPersonasQueMasDenunciaron,
    PersonaDenuncianteItem
)


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
            labels.append(item['persona'])
            data.append(item['cantidad_denuncias'])
            
            # Crear item completo
            personas_items.append(PersonaDenuncianteItem(
                persona=item['persona'],
                cantidad_denuncias=item['cantidad_denuncias']
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

