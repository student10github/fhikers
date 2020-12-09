sudo su postgres
psql

-- Cambiar el OWNER de una base de datos - Referencia: https://www.realsystems.com.mx/blog/postgresql-13/post/como-cambiar-el-dueno-a-todas-las-tablas-de-una-base-de-datos-postgresql-309
-- ALTER DATABASE $BASEDEDATOS OWNER TO $USER;
ALTER DATABASE test2_db OWNER TO test2_user;

CTRL + d
CTRL + d

psql -U test2_user postgres

DROP DATABASE test2_db;



-- el usuario test2_user no tiene permisos para crear base de datos
-- Cambiamos al usuario postgres y creamos la tabla
CTRL + d
sudo su postgres
psql

CREATE DATABASE fhikers_db;
GRANT ALL PRIVILEGES ON DATABASE fhikers_db TO fhikers_user;

psql -U fhikers_user fhikers_db