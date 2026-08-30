CREATE TABLE CAR_TYPE(
ID INTEGER PRIMARY KEY,
MAKE VARCHAR(25) NOT NULL,
MODEL VARCHAR(25) NOT NULL,
YEAR INTEGER NOT NULL
);

CREATE TABLE CAR(
VIN VARCHAR(25) PRIMARY KEY,
COLOR VARCHAR(25) NOT NULL,
ID_CAR_TYPE INTEGER REFERENCES CAR_TYPE,
ID_INSURANCE_POLICY INTEGER REFERENCES INSURANCE_POLICY
);

CREATE TABLE INSURANCE_COMPANY(
ID INTEGER PRIMARY KEY,
COMPANY_NAME VARCHAR(25) NOT NULL
);

CREATE TABLE INSURANCE_POLICY(
ID INTEGER PRIMARY KEY,
POLICY_NAME VARCHAR(25) NOT NULL,
ID_INSURANCE_COMPANY INTEGER REFERENCES INSURANCE_COMPANY
);

CREATE TABLE OWNER(
ID INTEGER PRIMARY KEY,
OWNER_NAME VARCHAR(25) NOT NULL,
OWNER_PHONE VARCHAR(25) NOT NULL
);

CREATE TABLE OWNER_CAR(
VIN VARCHAR(25) REFERENCES CAR,
ID_OWNER INTEGER REFERENCES OWNER
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