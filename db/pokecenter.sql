DROP TABLE IF EXISTS pokemons;
DROP TABLE IF EXISTS nurses;
DROP TABLE IF EXISTS trainers;

CREATE TABLE nurses ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    specialisation VARCHAR(255)
);

CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    number INT
);

CREATE TABLE pokemons ( 
    id SERIAL PRIMARY KEY,
    nickname VARCHAR(255),
    species VARCHAR(255),
    type VARCHAR(255),
    dob VARCHAR(255),
    status VARCHAR(255),
    trainer_id INT REFERENCES trainers(id) ON DELETE CASCADE,
    nurse_id INT REFERENCES nurses(id) ON DELETE CASCADE 
);
