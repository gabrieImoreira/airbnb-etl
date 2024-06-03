-- Conecte-se ao banco de dados airbnb_rooms_gams antes de executar isso

CREATE TABLE IF NOT EXISTS airbnb_rooms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    host_id INTEGER,
    host_name VARCHAR(255),
    neighbourhood_group VARCHAR(255),
    neighbourhood VARCHAR(255),
    room_type VARCHAR(255),
    price INTEGER,
    currency VARCHAR(255),
    minimum_nights INTEGER,
    number_of_reviews INTEGER,
    last_review TIMESTAMP,
    rating REAL,
    bedrooms INTEGER,
    beds INTEGER,
    baths INTEGER,
    execution_date TIMESTAMP,
    origin VARCHAR(255)
);

INSERT INTO airbnb_rooms (name, host_id, host_name, neighbourhood_group, neighbourhood, room_type, price, currency, minimum_nights, number_of_reviews, last_review, rating, bedrooms, beds, baths, execution_date, origin)
VALUES ('Casa de Praia', 1, 'João', 'Zona Sul', 'Copacabana', 'Casa', 1000, 'BRL', 2, 10, '2024-04-28 14:30:00', 4.5, 2, 3, 2, '2024-04-28 14:30:00', 'teste');

INSERT INTO airbnb_rooms (name, host_id, host_name, neighbourhood_group, neighbourhood, room_type, price, currency, minimum_nights, number_of_reviews, last_review, rating, bedrooms, beds, baths, execution_date, origin)
VALUES ('Casa de Campo', 2, 'Maria', 'Zona Oeste', 'Barra da Tijuca', 'Casa', 2000, 'BRL', 3, 20, '2024-04-28 14:30:00', 4.8, 3, 4, 3, '2024-04-28 14:30:00', 'teste');