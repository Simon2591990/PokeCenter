DROP TABLE IF EXISTS pokemons;
DROP TABLE IF EXISTS nurses;


CREATE TABLE nurses ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE pokemons ( 
    id SERIAL PRIMARY KEY,
    nickname VARCHAR(255),
    species VARCHAR(255),
    type VARCHAR(255),
    dob VARCHAR(255),
    status VARCHAR(255),
    trainer_id INT REFERENCES trainer(id) ON DELETE CASCADE
    nurse_id INT REFERENCES nurses(id) ON DELETE CASCADE 
);

CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    number INT
);