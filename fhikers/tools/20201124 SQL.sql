sudo su postgres
psql

CREATE USER test2_user WITH PASSWORD 'patata';

CREATE DATABASE test2_db;

GRANT ALL PRIVILEGES ON DATABASE test2_db TO test2_user;

-- Cambiar base de datos
\c test2_db;

-- Cambiar de usuario
SET SESSION AUTHORIZATION test2_user;

-- Verificar usuario y base de datos actuales
SELECT CURRENT_USER, SESSION_USER;

-- para salir
CTRL + D
CTRL + D

-- opción para acceder a una base de datos con un usuario determinados desde la terminal fuera del postgres
psql -U test2_user test2_db

-- para salir de la visualizacion de una tabla
q

-- para interromper un comando que no se realiza
CTRL + C

-- Para salir de la base de datos actual
CTRL + D