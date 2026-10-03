SET search_path TO shop;

INSERT INTO USERS (DNI, NAME, EMAIL, PHONE, ADDRESS) VALUES
('1111111', 'Miguel Oviedo Rojas', 'miguel@gmail.com', '1111-1111', 'Costa Rica'),
('2222222', 'Magaly Benavides Espinoza', 'magaly@hotmail.com', '2222-2222', 'Panama'),
('3333333', 'Yamileth Rojas Campos', 'yamileth@outlook.com', '3333-3333', 'USA');


INSERT INTO PRODUCTS (DESCRIPTION, PRICE, STOCK, BRAND) VALUES
('LAPTOP', 1000.00, 3, 'DELL'),
('TABLET', 500.00, 6, 'LENOVO'),
('MOUSE', 200.00, 15, 'LOGITECH');