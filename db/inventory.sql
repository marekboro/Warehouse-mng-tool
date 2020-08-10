DROP TABLE stock;
DROP TABLE products;
DROP TABLE types;
DROP TABLE brands;


CREATE TABLE brands(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    warranty_details TEXT
);

CREATE TABLE types(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    product_type_id SERIAL REFERENCES types(id) ON DELETE CASCADE,
    brand_id SERIAL REFERENCES brands(id) ON DELETE CASCADE,
    description TEXT,
    distributor_price FLOAT,
    sale_price FLOAT,
    warranty_length INT
);

CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    product_id SERIAL REFERENCES products(id) ON DELETE CASCADE,
    product_type_id SERIAL REFERENCES types(id),
    brand_id SERIAL REFERENCES brands(id),
    count INT
);

-- NOTE TO SELF!  ALWAYS USE   createdb database_name  in CONSOLE!  - to create the database before working on it
-- psql -d inventory -f db/inventory.sql in console to create the tables