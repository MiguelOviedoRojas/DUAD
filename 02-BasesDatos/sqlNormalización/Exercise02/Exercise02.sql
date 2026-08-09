CREATE TABLE CARS(
VIN INTEGER PRIMARY KEY,
MAKE VARCHAR(25) NOT NULL,
MODEL VARCHAR(25) NOT NULL,
YEAR DATE NOT NULL,
COLOR VARCHAR(25) NOT NULL
);

CREATE TABLE OWNERS(
ID_OWNER INTEGER PRIMARY KEY,
OWNER_NAME VARCHAR(25) NOT NULL,
ONWER_PHONE INTEGER NOT NULL,
ID_INSURANCE INTEGER REFERENCES INSURANCE
);

CREATE TABLE INSURANCE(
ID_INSURANCE INTEGER PRIMARY KEY,
INSURANCE_COMPANY VARCHAR(25) NOT NULL,
INSURANCE_POLICY VARCHAR(25) NOT NULL
);

CREATE TABLE OWNER_CAR(
ID_OWNERCAR INTEGER PRIMARY KEY,
VIN INTEGER REFERENCES CARS,
ID_OWNER INTEGER REFERENCES OWNERS
);

1FN
La tabla presenta redundancia de información. Los datos del vehículo, del propietario y del seguro se almacenan repetidamente,
lo que puede generar inconsistencias cuando se requieran actualizaciones.

2FN
Durante el análisis se identificaron diferentes grupos de información.
Por lo tanto se decidió separarlos en tablas independientes, y con esta separación se evitar repetir información del vehículo.

3FN
Después de separar las entidades principales, se identificó que existe una relación entre vehículos y propietarios.
En los datos originales se observa que un mismo vehículo puede estar asociado a más de un propietario.