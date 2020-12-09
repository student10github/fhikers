sudo su postgres
psql

CREATE USER proyecto_user WITH PASSWORD 'patata';

CREATE DATABASE proyecto_db;

GRANT ALL PRIVILEGES ON DATABASE proyecto_db TO proyecto_user;

-- Cambiar base de datos
\c proyecto_db;

-- Cambiar de usuario
SET SESSION AUTHORIZATION proyecto_user;

-- Verificar usuario y base de datos actuales
SELECT CURRENT_USER, SESSION_USER;

-- para salir
CTRL + D
CTRL + D

-- opción para acceder a una base de datos con un usuario determinados desde la terminal fuera del postgres
psql -U proyecto_user proyecto_db