# ============================================
# Función para actualizar metadata (agregar a tu script de carga)
# ============================================

def actualizar_metadata_ultima_actualizacion(conn):
    """
    Actualiza la fecha de última actualización en la tabla metadata.
    Esta función debe llamarse al final del proceso de carga exitoso.
    
    Args:
        conn: Conexión a la base de datos (psycopg2)
    """
    try:
        with conn.cursor() as cur:
            # Insertar o actualizar la fecha de última actualización
            cur.execute("""
                INSERT INTO metadata (clave, valor)
                VALUES ('ultima_actualizacion', NOW())
                ON CONFLICT (clave) 
                DO UPDATE SET valor = NOW()
            """)
        conn.commit()
        print("✅ Fecha de última actualización actualizada en metadata")
    except Exception as e:
        conn.rollback()
        print(f"⚠️ Advertencia: No se pudo actualizar metadata: {e}")
        # No lanzamos excepción para no interrumpir el proceso si falla esto

