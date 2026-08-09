CREATE TABLE CUSTOMER(
ID INTEGER PRIMARY KEY,
NAME VARCHAR (25) NOT NULL,
PHONE INTEGER NOT NULL
);

CREATE TABLE ITEMS(
ID INTEGER PRIMARY KEY,
ITEM_NAME VARCHAR(25) NOT NULL,
PRICE FLOAT NOT NULL
);

CREATE TABLE ORDERS(
ID INTEGER PRIMARY KEY,
ID_CUSTOMER INTEGER REFERENCES CUSTOMER(ID),
ADDRESS VARCHAR(25) NOT NULL,
DELIVERY_TIME DATE TIME NOT NULL
);

CREATE TABLE ORDER_ITEM(
ID INTEGER PRIMARY KEY,
ID_ORDER INTEGER REFERENCES ORDERS(ID),
ID_ITEM INTEGER REFERENCES ITEMS(ID),
QUANTITY INTEGER DEFAULT 0,
SPECIAL_REQUEST VARCHAR(25) DEFAULT "-"
);


Justificacion:
* Se repiten datos de clientes.
* Se repiten datos de productos.
* Un pedido contiene varios productos.
* Un producto aparece en varios pedidos.
* Hay redundancia de dirección y hora de entrega.

1FN
La tabla original se encuentra en Primera Forma Normal (1FN) porque todos sus atributos contienen valores atómicos, es decir,
cada columna almacena un único valor y no existen listas o grupos repetitivos dentro de una misma celda.

2FN
La Segunda Forma Normal elimina las dependencias parciales sobre una clave compuesta.
Por lo tanto, se separaron en tablas independientes.

3FN
La tabla original contenía información de clientes, pedidos y productos en una sola estructura. Esto provocaba repetición de datos,
ya que un mismo cliente podía aparecer en varios registros y un mismo producto podía formar parte de diferentes pedidos.