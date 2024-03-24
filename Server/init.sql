DO
$do$
BEGIN
   IF EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE  rolname = 'toto') THEN

      RAISE NOTICE 'Role "toto" already exists. Skipping.';
   ELSE
      CREATE ROLE toto LOGIN PASSWORD 'unGrosMotDePasse';
   END IF;
END
$do$;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR (50) UNIQUE NOT NULL,
  password VARCHAR (50) NOT NULL,
  first_name VARCHAR (50) NOT NULL,
  last_name VARCHAR (50) NOT NULL,
  email VARCHAR (255) UNIQUE NOT NULL
);

INSERT INTO users (id, username, password, email, first_name, last_name)
VALUES (1234, 'toto', 'grosMotDePasse', 'toto@toto.com', 'toto', 'toto');
