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
    type_id SERIAL REFERENCES types(id),
    brand_id SERIAL REFERENCES brands(id),
    description TEXT,
    distributor_price FLOAT,
    sale_price FLOAT,
    warranty_length INT
);

CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    product_id SERIAL REFERENCES products(id)
);
