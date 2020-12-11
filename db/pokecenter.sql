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
    trainer_name VARCHAR(255),
    trainer_number INT,
    status VARCHAR(255),
    nurse_id INT REFERENCES nurses(id) ON DELETE CASCADE 
);