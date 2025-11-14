from typing import List, Dict, Any, Generator
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.core.database import SessionLocal


class JuezRepository:
    """
    Repository para consultas de solo lectura relacionadas con Jueces.
    Solo proporciona métodos para obtener datos, no para modificar.
    """
    
    def __init__(self, db: Session):
        """
        Inicializa el repository con una sesión de base de datos.
        
        Args:
            db: Sesión de SQLAlchemy
        """
        self.db = db
    
    def get_jueces_con_mayor_demora(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Obtiene los jueces con mayor demora promedio en sus expedientes.
        
        Calcula la duración promedio de expedientes por juez basándose en:
        - Diferencia entre fecha_ultimo_movimiento y fecha_inicio
        - Agrupa por juez y tribunal
        - Ordena por demora promedio descendente
        
        Args:
            limit: Número máximo de resultados a retornar (default: 10)
            
        Returns:
            Lista de diccionarios con:
            - juez_nombre: Nombre del juez
            - tribunal_nombre: Nombre del tribunal
            - demora_promedio_dias: Promedio de días de demora (redondeado a 2 decimales)
            - cantidad_expedientes: Cantidad de expedientes del juez
        """
        query = text("""
            WITH duraciones AS (
                SELECT 
                    e.numero_expediente,
                    e.id_tribunal,
                    (e.fecha_ultimo_movimiento::date - e.fecha_inicio::date) AS dias_duracion
                FROM expediente e
                WHERE e.fecha_inicio IS NOT NULL 
                  AND e.fecha_ultimo_movimiento IS NOT NULL
            ),
            demoras_jueces AS (
                SELECT 
                    j.juez_id,
                    j.nombre AS juez_nombre,
                    t.nombre AS tribunal_nombre,
                    AVG(d.dias_duracion) AS demora_promedio_dias,
                    COUNT(d.numero_expediente) AS cantidad_expedientes
                FROM duraciones d
                JOIN tribunal t ON d.id_tribunal = t.tribunal_id
                JOIN tribunal_juez tj ON tj.tribunal_id = t.tribunal_id
                JOIN juez j ON j.juez_id = tj.juez_id
                GROUP BY j.juez_id, j.nombre, t.nombre
            )
            SELECT 
                juez_nombre,
                tribunal_nombre,
                ROUND(demora_promedio_dias, 2) AS demora_promedio_dias,
                cantidad_expedientes
            FROM demoras_jueces
            ORDER BY demora_promedio_dias DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        
        # Convertir resultados a lista de diccionarios
        jueces = []
        for row in result:
            jueces.append({
                "juez_nombre": row.juez_nombre,
                "tribunal_nombre": row.tribunal_nombre,
                "demora_promedio_dias": float(row.demora_promedio_dias),
                "cantidad_expedientes": int(row.cantidad_expedientes)
            })
        
        return jueces


def get_juez_repository() -> Generator[JuezRepository, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del JuezRepository.
    Crea una nueva sesión de base de datos y la cierra automáticamente.
    
    Yields:
        Instancia de JuezRepository
        
    Usage en FastAPI:
        @app.get("/jueces/mayor-demora")
        def get_jueces(repo: JuezRepository = Depends(get_juez_repository)):
            return repo.get_jueces_con_mayor_demora()
    """
    db = SessionLocal()
    try:
        yield JuezRepository(db)
    finally:
        db.close()
