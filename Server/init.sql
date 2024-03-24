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
