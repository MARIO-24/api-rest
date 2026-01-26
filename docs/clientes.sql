CREATE DATABASE gym;
USE gym;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100),
    telefono VARCHAR(20),
    fecha_nacimiento DATE,
    genero VARCHAR(20),
    tipo_membresia VARCHAR(30),
    fecha_alta DATETIME DEFAULT CURRENT_TIMESTAMP,
    activo INT
);
