from typing import List, Optional, Generator, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc, asc, text
from datetime import date, datetime

from app.core.database import SessionLocal
from app.models.expediente import Expediente


class ExpedienteRepository:
    """
    Repository para consultas de solo lectura de Expediente.
    Solo proporciona métodos para obtener datos, no para modificar.
    """
    
    def __init__(self, db: Session):
        """
        Inicializa el repository con una sesión de base de datos.
        
        Args:
            db: Sesión de SQLAlchemy
        """
        self.db = db
    
    def get_by_numero(self, numero_expediente: str) -> Optional[Expediente]:
        """
        Obtiene un expediente por su número de expediente.
        
        Args:
            numero_expediente: Número del expediente (PK)
            
        Returns:
            Expediente o None si no existe
        """
        return self.db.query(Expediente).filter(
            Expediente.numero_expediente == numero_expediente
        ).first()
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Expediente]:
        """
        Obtiene todos los expedientes con paginación.
        
        Args:
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes
        """
        return self.db.query(Expediente).offset(skip).limit(limit).all()
    
    def get_by_estado_procesal(
        self, 
        estado_procesal: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por estado procesal.
        
        Args:
            estado_procesal: Estado procesal ('En trámite' o 'Terminada')
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes con el estado procesal especificado
        """
        return self.db.query(Expediente).filter(
            Expediente.estado_procesal == estado_procesal
        ).offset(skip).limit(limit).all()
    
    def get_by_tribunal(
        self, 
        tribunal_id: int, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por tribunal.
        
        Args:
            tribunal_id: ID del tribunal
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes del tribunal
        """
        return self.db.query(Expediente).filter(
            Expediente.id_tribunal == tribunal_id
        ).offset(skip).limit(limit).all()
    
    def get_by_jurisdiccion(
        self, 
        jurisdiccion: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por jurisdicción.
        
        Args:
            jurisdiccion: Nombre de la jurisdicción
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes de la jurisdicción
        """
        return self.db.query(Expediente).filter(
            Expediente.jurisdiccion.ilike(f"%{jurisdiccion}%")
        ).offset(skip).limit(limit).all()
    
    def search_by_numero(self, numero: str) -> List[Expediente]:
        """
        Busca expedientes por número de expediente (búsqueda parcial).
        
        Args:
            numero: Número o parte del número de expediente
            
        Returns:
            Lista de expedientes que coinciden
        """
        return self.db.query(Expediente).filter(
            Expediente.numero_expediente.ilike(f"%{numero}%")
        ).all()
    
    def search_by_caratula(self, caratula: str, skip: int = 0, limit: int = 100) -> List[Expediente]:
        """
        Busca expedientes por carátula (búsqueda parcial).
        
        Args:
            caratula: Texto a buscar en la carátula
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes que coinciden
        """
        return self.db.query(Expediente).filter(
            Expediente.caratula.ilike(f"%{caratula}%")
        ).offset(skip).limit(limit).all()
    
    def get_by_fecha_inicio_range(
        self, 
        fecha_inicio: date, 
        fecha_fin: date, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes en un rango de fechas de inicio.
        
        Args:
            fecha_inicio: Fecha de inicio
            fecha_fin: Fecha de fin
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes en el rango de fechas
        """
        return self.db.query(Expediente).filter(
            and_(
                Expediente.fecha_inicio >= fecha_inicio,
                Expediente.fecha_inicio <= fecha_fin
            )
        ).offset(skip).limit(limit).all()
    
    def get_by_ano_inicio(
        self, 
        ano: int, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes por año de inicio.
        
        Args:
            ano: Año de inicio
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes del año especificado
        """
        return self.db.query(Expediente).filter(
            Expediente.ano_inicio == ano
        ).offset(skip).limit(limit).all()
    
    def get_by_fiscal(
        self, 
        fiscal: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por fiscal.
        
        Args:
            fiscal: Nombre del fiscal
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes del fiscal
        """
        return self.db.query(Expediente).filter(
            Expediente.fiscal.ilike(f"%{fiscal}%")
        ).offset(skip).limit(limit).all()
    
    def get_by_fiscalia(
        self, 
        fiscalia: str, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Expediente]:
        """
        Obtiene expedientes filtrados por fiscalía.
        
        Args:
            fiscalia: Nombre de la fiscalía
            skip: Número de registros a saltar
            limit: Número máximo de registros a retornar
            
        Returns:
            Lista de expedientes de la fiscalía
        """
        return self.db.query(Expediente).filter(
            Expediente.fiscalia.ilike(f"%{fiscalia}%")
        ).offset(skip).limit(limit).all()
    
    def count(self) -> int:
        """
        Cuenta el total de expedientes.
        
        Returns:
            Número total de expedientes
        """
        return self.db.query(Expediente).count()
    
    def count_by_estado_procesal(self, estado_procesal: str) -> int:
        """
        Cuenta expedientes por estado procesal.
        
        Args:
            estado_procesal: Estado procesal ('En trámite' o 'Terminada')
            
        Returns:
            Número de expedientes con el estado especificado
        """
        return self.db.query(Expediente).filter(
            Expediente.estado_procesal == estado_procesal
        ).count()
    
    def count_by_tribunal(self, tribunal_id: int) -> int:
        """
        Cuenta expedientes por tribunal.
        
        Args:
            tribunal_id: ID del tribunal
            
        Returns:
            Número de expedientes del tribunal
        """
        return self.db.query(Expediente).filter(
            Expediente.id_tribunal == tribunal_id
        ).count()
    
    def count_by_ano_inicio(self, ano: int) -> int:
        """
        Cuenta expedientes por año de inicio.
        
        Args:
            ano: Año de inicio
            
        Returns:
            Número de expedientes del año especificado
        """
        return self.db.query(Expediente).filter(
            Expediente.ano_inicio == ano
        ).count()
    
    def count_by_year(self) -> List[Dict[str, Any]]:
        """
        Obtiene la cantidad de causas iniciadas por año, separadas por estado procesal.
        
        Returns:
            Lista de diccionarios con:
            - anio: Año de inicio
            - cantidad_causas_abiertas: Cantidad de causas en trámite iniciadas en ese año
            - cantidad_causas_terminadas: Cantidad de causas terminadas iniciadas en ese año
            - cantidad_causas: Total de causas iniciadas en ese año
        """
        query = text("""
            SELECT 
                ano_inicio AS anio,
                COUNT(CASE WHEN estado_procesal = 'En trámite' THEN 1 END) AS cantidad_causas_abiertas,
                COUNT(CASE WHEN estado_procesal = 'Terminada' THEN 1 END) AS cantidad_causas_terminadas,
                COUNT(*) AS cantidad_causas
            FROM expediente
            WHERE ano_inicio IS NOT NULL
            GROUP BY ano_inicio
            ORDER BY anio
        """)
        
        result = self.db.execute(query)
        
        # Convertir resultados a lista de diccionarios
        datos_por_ano = []
        for row in result:
            datos_por_ano.append({
                "anio": int(row.anio),
                "cantidad_causas_abiertas": int(row.cantidad_causas_abiertas),
                "cantidad_causas_terminadas": int(row.cantidad_causas_terminadas),
                "cantidad_causas": int(row.cantidad_causas)
            })
        
        return datos_por_ano
    
    def get_delitos_mas_frecuentes(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Obtiene los delitos más frecuentes, separados por estado procesal.
        
        Args:
            limit: Número máximo de resultados a retornar (default: 10)
            
        Returns:
            Lista de diccionarios con:
            - delito: Nombre del tipo de delito
            - cantidad_causas_abiertas: Cantidad de causas en trámite con ese delito
            - cantidad_causas_terminadas: Cantidad de causas terminadas con ese delito
            - cantidad_causas: Total de causas con ese delito
        """
        # Usar las tablas relacionales (expediente_delito, tipo_delito) con estado procesal
        query_relacional = text("""
            SELECT 
                td.nombre AS delito,
                COUNT(CASE WHEN e.estado_procesal = 'En trámite' THEN 1 END) AS cantidad_causas_abiertas,
                COUNT(CASE WHEN e.estado_procesal = 'Terminada' THEN 1 END) AS cantidad_causas_terminadas,
                COUNT(ed.numero_expediente) AS cantidad_causas
            FROM expediente_delito ed
            JOIN tipo_delito td ON ed.tipo_delito_id = td.tipo_delito_id
            JOIN expediente e ON ed.numero_expediente = e.numero_expediente
            GROUP BY td.nombre
            ORDER BY cantidad_causas DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query_relacional, {"limit": limit})
        delitos = []
        for row in result:
            delitos.append({
                "delito": row.delito,
                "cantidad_causas_abiertas": int(row.cantidad_causas_abiertas),
                "cantidad_causas_terminadas": int(row.cantidad_causas_terminadas),
                "cantidad_causas": int(row.cantidad_causas)
            })
        
        return delitos
    
    def get_causas_por_juzgado(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Obtiene la cantidad de causas agrupadas por juzgado/tribunal, separadas por estado procesal.
        
        Args:
            limit: Número máximo de resultados a retornar (default: 20)
            
        Returns:
            Lista de diccionarios con:
            - tribunal: Nombre del tribunal/juzgado
            - cantidad_causas_abiertas: Cantidad de causas en trámite
            - cantidad_causas_terminadas: Cantidad de causas terminadas
            - cantidad_causas: Total de causas
        """
        # Usar el campo TEXT tribunal directamente (no hay FK id_tribunal)
        query = text("""
            WITH tribunales_limpios AS (
                SELECT 
                    REGEXP_REPLACE(
                        REGEXP_REPLACE(
                            REGEXP_REPLACE(
                                REGEXP_REPLACE(
                                    TRIM(tribunal),
                                    '^Dr\.?\s+', '', 'g'
                                ),
                                '^Dra\.?\s+', '', 'g'
                            ),
                            '^DR\.?\s+', '', 'g'
                        ),
                        '^DRA\.?\s+', '', 'g'
                    ) AS tribunal_limpio,
                    estado_procesal
                FROM expediente
                WHERE tribunal IS NOT NULL 
                  AND tribunal != ''
            )
            SELECT 
                REGEXP_REPLACE(
                    REGEXP_REPLACE(
                        REPLACE(
                            REPLACE(tribunal_limpio, ' LO ', ' Lo '),
                            ' LOS ', ' Los '
                        ),
                        '^LO ', 'Lo ', 'g'
                    ),
                    '^LOS ', 'Los ', 'g'
                ) AS tribunal,
                COUNT(CASE WHEN estado_procesal = 'En trámite' THEN 1 END) AS cantidad_causas_abiertas,
                COUNT(CASE WHEN estado_procesal = 'Terminada' THEN 1 END) AS cantidad_causas_terminadas,
                COUNT(*) AS cantidad_causas
            FROM tribunales_limpios
            GROUP BY tribunal_limpio
            ORDER BY cantidad_causas DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        tribunales = []
        for row in result:
            tribunales.append({
                "tribunal": row.tribunal,
                "cantidad_causas_abiertas": int(row.cantidad_causas_abiertas),
                "cantidad_causas_terminadas": int(row.cantidad_causas_terminadas),
                "cantidad_causas": int(row.cantidad_causas)
            })
        
        return tribunales
    
    def get_causas_terminadas_por_juzgado(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Obtiene la cantidad de causas terminadas agrupadas por juzgado/tribunal.
        
        Args:
            limit: Número máximo de resultados a retornar (default: 20)
            
        Returns:
            Lista de diccionarios con:
            - tribunal: Nombre del tribunal/juzgado
            - cantidad_causas_terminadas: Cantidad de causas terminadas
        """
        # Usar el campo TEXT tribunal directamente (no hay FK id_tribunal)
        query = text("""
            SELECT 
                tribunal,
                COUNT(*) AS cantidad_causas_terminadas
            FROM expediente
            WHERE estado_procesal = 'Terminada'
              AND tribunal IS NOT NULL 
              AND tribunal != ''
            GROUP BY tribunal
            ORDER BY cantidad_causas_terminadas DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        tribunales = []
        for row in result:
            tribunales.append({
                "tribunal": row.tribunal,
                "cantidad_causas_terminadas": int(row.cantidad_causas_terminadas)
            })
        
        return tribunales
    
    def get_causas_por_fuero(self) -> List[Dict[str, Any]]:
        """
        Obtiene la cantidad de causas agrupadas por fuero judicial, separadas por estado procesal.
        
        Returns:
            Lista de diccionarios con:
            - fuero: Nombre del fuero judicial
            - cantidad_causas_abiertas: Cantidad de causas en trámite en ese fuero
            - cantidad_causas_terminadas: Cantidad de causas terminadas en ese fuero
            - cantidad_causas: Total de causas en ese fuero
        """
        query = text("""
            SELECT 
                t.fuero AS fuero,
                COUNT(CASE WHEN e.estado_procesal = 'En trámite' THEN 1 END) AS cantidad_causas_abiertas,
                COUNT(CASE WHEN e.estado_procesal = 'Terminada' THEN 1 END) AS cantidad_causas_terminadas,
                COUNT(e.numero_expediente) AS cantidad_causas
            FROM expediente e
            JOIN tribunal t ON e.tribunal = t.nombre
            WHERE t.fuero IS NOT NULL
            GROUP BY t.fuero
            ORDER BY cantidad_causas DESC
        """)
        
        result = self.db.execute(query)
        fueros = []
        for row in result:
            fueros.append({
                "fuero": row.fuero,
                "cantidad_causas_abiertas": int(row.cantidad_causas_abiertas),
                "cantidad_causas_terminadas": int(row.cantidad_causas_terminadas),
                "cantidad_causas": int(row.cantidad_causas)
            })
        
        return fueros
    
    def get_causas_por_fiscalia(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        Obtiene la cantidad de causas agrupadas por fiscalía, clasificadas por estado procesal.
        
        Args:
            limit: Número máximo de fiscalías a retornar (default: 20)
            
        Returns:
            Lista de diccionarios con:
            - fiscalia: Nombre de la fiscalía
            - causas_abiertas: Cantidad de causas en trámite (abiertas)
            - causas_terminadas: Cantidad de causas terminadas
            - total_causas: Total de causas de la fiscalía
        """
        query = text("""
            WITH fiscalias_limpias AS (
                SELECT 
                    REGEXP_REPLACE(
                        REGEXP_REPLACE(
                            REPLACE(
                                REPLACE(TRIM(fiscalia), ' LO ', ' Lo '),
                                ' LOS ', ' Los '
                            ),
                            '^LO ', 'Lo ', 'g'
                        ),
                        '^LOS ', 'Los ', 'g'
                    ) AS fiscalia_limpia,
                    estado_procesal
                FROM expediente
                WHERE fiscalia IS NOT NULL AND fiscalia != ''
            )
            SELECT 
                fiscalia_limpia AS fiscalia,
                COUNT(CASE WHEN estado_procesal = 'En trámite' THEN 1 END) AS causas_abiertas,
                COUNT(CASE WHEN estado_procesal = 'Terminada' THEN 1 END) AS causas_terminadas,
                COUNT(*) AS total_causas
            FROM fiscalias_limpias
            GROUP BY fiscalia_limpia
            ORDER BY total_causas DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        
        # Convertir resultados a lista de diccionarios
        fiscalias = []
        for row in result:
            fiscalias.append({
                "fiscalia": row.fiscalia,
                "causas_abiertas": int(row.causas_abiertas),
                "causas_terminadas": int(row.causas_terminadas),
                "total_causas": int(row.total_causas)
            })
        
        return fiscalias
    
    def get_duracion_instruccion(self, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Obtiene las causas ordenadas por duración de instrucción (de más larga a más corta).
        Calcula la duración como la diferencia entre fecha_ultimo_movimiento y fecha_inicio.
        
        Args:
            limit: Número máximo de resultados a retornar (default: 50)
            
        Returns:
            Lista de diccionarios con:
            - numero_expediente: Número del expediente
            - caratula: Carátula del expediente
            - tribunal: Nombre del tribunal
            - estado_procesal: Estado procesal
            - fecha_inicio: Fecha de inicio
            - fecha_ultimo_movimiento: Fecha del último movimiento
            - duracion_dias: Duración en días
        """
        query = text("""
            SELECT 
                e.numero_expediente,
                e.caratula,
                e.tribunal,
                e.estado_procesal,
                e.fecha_inicio,
                e.fecha_ultimo_movimiento,
                (e.fecha_ultimo_movimiento::date - e.fecha_inicio::date) AS duracion_dias
            FROM expediente e
            WHERE 
                e.fecha_inicio IS NOT NULL
                AND e.fecha_ultimo_movimiento IS NOT NULL
            ORDER BY duracion_dias DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        
        # Convertir resultados a lista de diccionarios
        causas = []
        for row in result:
            causas.append({
                "numero_expediente": row.numero_expediente,
                "caratula": row.caratula,
                "tribunal": row.tribunal,
                "estado_procesal": row.estado_procesal,
                "fecha_inicio": row.fecha_inicio.isoformat() if row.fecha_inicio else None,
                "fecha_ultimo_movimiento": row.fecha_ultimo_movimiento.isoformat() if row.fecha_ultimo_movimiento else None,
                "duracion_dias": int(row.duracion_dias) if row.duracion_dias else 0
            })
        
        return causas
    
    def get_duracion_promedio_global(self) -> Dict[str, Any]:
        """
        Calcula la duración promedio, máxima y mínima de TODAS las causas
        que tienen fecha_inicio y fecha_ultimo_movimiento.
        Este método calcula estadísticas globales sin limitar por cantidad.
        
        Returns:
            Diccionario con:
            - duracion_promedio_dias: Duración promedio en días (float)
            - duracion_maxima_dias: Duración máxima en días (int)
            - duracion_minima_dias: Duración mínima en días (int)
            - total_causas: Total de causas analizadas (int)
        """
        query = text("""
            SELECT 
                AVG((fecha_ultimo_movimiento::date - fecha_inicio::date)) AS duracion_promedio_dias,
                MAX((fecha_ultimo_movimiento::date - fecha_inicio::date)) AS duracion_maxima_dias,
                MIN((fecha_ultimo_movimiento::date - fecha_inicio::date)) AS duracion_minima_dias,
                COUNT(*) AS total_causas
            FROM expediente
            WHERE 
                fecha_inicio IS NOT NULL
                AND fecha_ultimo_movimiento IS NOT NULL
        """)
        
        result = self.db.execute(query).first()
        
        if result and result.total_causas > 0:
            return {
                "duracion_promedio_dias": float(result.duracion_promedio_dias) if result.duracion_promedio_dias else 0.0,
                "duracion_maxima_dias": int(result.duracion_maxima_dias) if result.duracion_maxima_dias else 0,
                "duracion_minima_dias": int(result.duracion_minima_dias) if result.duracion_minima_dias else 0,
                "total_causas": int(result.total_causas)
            }
        else:
            return {
                "duracion_promedio_dias": 0.0,
                "duracion_maxima_dias": 0,
                "duracion_minima_dias": 0,
                "total_causas": 0
            }
    
    def get_duracion_outliers_mas_largos(self, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Obtiene las causas con mayor duración de instrucción (outliers superiores).
        Incluye el nombre del imputado (denunciado) de cada causa.
        
        Args:
            limit: Número máximo de resultados a retornar (default: 5)
            
        Returns:
            Lista de diccionarios con:
            - numero_expediente: Número del expediente
            - caratula: Carátula del expediente
            - tribunal: Nombre del tribunal
            - estado_procesal: Estado procesal
            - fecha_inicio: Fecha de inicio
            - fecha_ultimo_movimiento: Fecha del último movimiento
            - duracion_dias: Duración en días
            - imputado_nombre: Nombre del imputado (denunciado) o None si no hay
        """
        query = text("""
            SELECT 
                e.numero_expediente,
                e.caratula,
                e.tribunal,
                e.estado_procesal,
                e.fecha_inicio,
                e.fecha_ultimo_movimiento,
                (e.fecha_ultimo_movimiento::date - e.fecha_inicio::date) AS duracion_dias,
                (
                    SELECT p.nombre_razon_social
                    FROM parte p
                    JOIN rol_parte rp ON rp.parte_id = p.parte_id
                    WHERE p.numero_expediente = e.numero_expediente
                      AND (UPPER(TRIM(rp.nombre)) = 'DENUNCIADO' OR UPPER(TRIM(rp.nombre)) = 'IMPUTADO')
                    LIMIT 1
                ) AS imputado_nombre
            FROM expediente e
            WHERE 
                e.fecha_inicio IS NOT NULL
                AND e.fecha_ultimo_movimiento IS NOT NULL
            ORDER BY duracion_dias DESC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        
        # Convertir resultados a lista de diccionarios
        causas = []
        for row in result:
            causas.append({
                "numero_expediente": row.numero_expediente,
                "caratula": row.caratula,
                "tribunal": row.tribunal,
                "estado_procesal": row.estado_procesal,
                "fecha_inicio": row.fecha_inicio.isoformat() if row.fecha_inicio else None,
                "fecha_ultimo_movimiento": row.fecha_ultimo_movimiento.isoformat() if row.fecha_ultimo_movimiento else None,
                "duracion_dias": int(row.duracion_dias) if row.duracion_dias else 0,
                "imputado_nombre": row.imputado_nombre if row.imputado_nombre else None
            })
        
        return causas
    
    def get_duracion_outliers_mas_cortos(self, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Obtiene las causas con menor duración de instrucción (outliers inferiores).
        Incluye el nombre del imputado (denunciado) de cada causa.
        
        Args:
            limit: Número máximo de resultados a retornar (default: 5)
            
        Returns:
            Lista de diccionarios con:
            - numero_expediente: Número del expediente
            - caratula: Carátula del expediente
            - tribunal: Nombre del tribunal
            - estado_procesal: Estado procesal
            - fecha_inicio: Fecha de inicio
            - fecha_ultimo_movimiento: Fecha del último movimiento
            - duracion_dias: Duración en días
            - imputado_nombre: Nombre del imputado (denunciado) o None si no hay
        """
        query = text("""
            SELECT 
                e.numero_expediente,
                e.caratula,
                e.tribunal,
                e.estado_procesal,
                e.fecha_inicio,
                e.fecha_ultimo_movimiento,
                (e.fecha_ultimo_movimiento::date - e.fecha_inicio::date) AS duracion_dias,
                (
                    SELECT p.nombre_razon_social
                    FROM parte p
                    JOIN rol_parte rp ON rp.parte_id = p.parte_id
                    WHERE p.numero_expediente = e.numero_expediente
                      AND (UPPER(TRIM(rp.nombre)) = 'DENUNCIADO' OR UPPER(TRIM(rp.nombre)) = 'IMPUTADO')
                    LIMIT 1
                ) AS imputado_nombre
            FROM expediente e
            WHERE 
                e.fecha_inicio IS NOT NULL
                AND e.fecha_ultimo_movimiento IS NOT NULL
            ORDER BY duracion_dias ASC
            LIMIT :limit
        """)
        
        result = self.db.execute(query, {"limit": limit})
        
        # Convertir resultados a lista de diccionarios
        causas = []
        for row in result:
            causas.append({
                "numero_expediente": row.numero_expediente,
                "caratula": row.caratula,
                "tribunal": row.tribunal,
                "estado_procesal": row.estado_procesal,
                "fecha_inicio": row.fecha_inicio.isoformat() if row.fecha_inicio else None,
                "fecha_ultimo_movimiento": row.fecha_ultimo_movimiento.isoformat() if row.fecha_ultimo_movimiento else None,
                "duracion_dias": int(row.duracion_dias) if row.duracion_dias else 0,
                "imputado_nombre": row.imputado_nombre
            })
        
        return causas
    
    def get_estadisticas_estado_procesal(self) -> dict:
        """
        Obtiene estadísticas de expedientes por estado procesal.
        
        Returns:
            Diccionario con conteos por estado procesal
        """
        total = self.count()
        en_tramite = self.count_by_estado_procesal('En trámite')
        terminada = self.count_by_estado_procesal('Terminada')
        
        return {
            'total': total,
            'en_tramite': en_tramite,
            'terminada': terminada,
            'porcentaje_en_tramite': (en_tramite / total * 100) if total > 0 else 0,
            'porcentaje_terminada': (terminada / total * 100) if total > 0 else 0
        }


def get_expediente_repository() -> Generator[ExpedienteRepository, None, None]:
    """
    Dependency de FastAPI para obtener una instancia del repository.
    Crea una nueva sesión de base de datos y la cierra automáticamente.
    
    Yields:
        Instancia de ExpedienteRepository
        
    Usage en FastAPI:
        @app.get("/expedientes")
        def get_expedientes(repo: ExpedienteRepository = Depends(get_expediente_repository)):
            return repo.get_all()
    """
    db = SessionLocal()
    try:
        yield ExpedienteRepository(db)
    finally:
        db.close()
