CREATE TABLE AUTHORS (
ID INTEGER PRIMARY KEY,
NAME VARCHAR(25) NOT NULL
);

CREATE TABLE BOOKS (
ID INTEGER PRIMARY KEY,
NAME VARCHAR(25) NOT NULL,
ID_AUTHOR INTEGER REFERENCES AUTHORS(ID)
);

CREATE TABLE CUSTOMERS (
ID INTEGER PRIMARY KEY,
NAME VARCHAR(25) NOT NULL,
EMAIL VARCHAR(50) NOT NULL
);

CREATE TABLE RENTS (
ID INTEGER PRIMARY KEY,
ID_BOOK INTEGER REFERENCES BOOKS(ID),
ID_CUSTOMER INTEGER REFERENCES CUSTOMERS(ID),
STATE VARCHAR(15) NOT NULL
);

INSERT INTO AUTHORS (ID, NAME) VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

INSERT INTO BOOKS (ID, NAME, ID_AUTHOR) VALUES
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The Book of the 5 Rings', NULL);

INSERT INTO CUSTOMERS (ID, NAME, EMAIL) VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');

INSERT INTO RENTS (ID, ID_BOOK, ID_CUSTOMER, STATE) VALUES
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');


--Querys

--1- Obtenga todos los libros y sus autores (en caso de tenerlos)
SELECT
BOOKS.NAME AS BOOK_NAME,
AUTHORS.NAME AS AUTHOR_NAME
FROM BOOKS
LEFT JOIN AUTHORS
ON AUTHORS.ID = BOOKS.ID_AUTHOR;

--2- Obtenga todos los libros que no tienen autor
SELECT NAME FROM BOOKS WHERE ID_AUTHOR IS NULL;

--3- Obtenga todos los autores que no tienen libros
SELECT AUTHORS.NAME
FROM AUTHORS
LEFT JOIN BOOKS
ON AUTHORS.ID = BOOKS.ID_AUTHOR
WHERE BOOKS.ID IS NULL;

--4- Obtenga todos los libros que han sido rentados en algún momento
SELECT DISTINCT BOOKS.NAME
FROM BOOKS
INNER JOIN RENTS
ON BOOKS.ID = RENTS.ID_BOOK;

--5- Obtenga todos los libros que nunca han sido rentados
SELECT BOOKS.NAME
FROM BOOKS
LEFT JOIN RENTS
ON BOOKS.ID = RENTS.ID_BOOK
WHERE RENTS.ID IS NULL;

--6- Obtenga todos los clientes que nunca han rentado un libro
SELECT CUSTOMERS.NAME
FROM CUSTOMERS
LEFT JOIN RENTS
ON CUSTOMERS.ID = RENTS.ID_CUSTOMER
WHERE RENTS.ID IS NULL;

--7- Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT DISTINCT BOOKS.NAME
FROM BOOKS
INNER JOIN RENTS
ON BOOKS.ID = RENTS.ID_BOOK
WHERE RENTS.STATE = 'Overdue';
