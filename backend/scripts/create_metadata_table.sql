-- Script para crear la tabla de metadatos
-- Ejecutar este script en la base de datos para crear la tabla metadata

CREATE TABLE IF NOT EXISTS metadata (
    clave VARCHAR(50) PRIMARY KEY,
    valor TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- Insertar registro inicial si no existe
INSERT INTO metadata (clave, valor)
VALUES ('ultima_actualizacion', NOW())
ON CONFLICT (clave) DO NOTHING;

