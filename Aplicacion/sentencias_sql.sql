CREATE TABLE Cliente(
    dni             INT         NOT NULL,
    nombre          VARCHAR     NOT NULL,
    apellido        VARCHAR     NOT NULL,
    celular         VARCHAR     NOT NULL,
    mail            VARCHAR     NOT NULL,
    departamento    VARCHAR     NOT NULL,
    calle           VARCHAR     NOT NULL,
    codigo_postal   VARCHAR     NOT NULL,
    apartamento     VARCHAR     NOT NULL,
    localidad       VARCHAR     NOT NULL,
    numero_puerta   VARCHAR     NOT NULL,
    CONSTRAINT  PKCliente
        Primary Key (dni)
);



CREATE TABLE Cuenta(
    numero_cuenta   BIGINT      NOT NULL,
    dni_cliente     INT         NOT NULL,
    usuario         VARCHAR     NOT NULL    UNIQUE,
    fecha_creacion  DATE        NOT NULL,
    CONSTRAINT PKCuenta
        Primary Key (numero_cuenta),
    CONSTRAINT  FKCuenta_Cliente
        Foreign Key (dni_cliente) References Cliente(dni)
);


CREATE TABLE Tarjeta(
    numero_tarjeta  INT         NOT NULL,
    tipo            VARCHAR     NOT NULL,
    vencimiento     DATE        NOT NULL,
    emisor          VARCHAR,
    numero_cuenta   BIGINT      NOT NULL,
    CONSTRAINT  PKTarjeta
        Primary Key (numero_tarjeta),
    CONSTRAINT  FKTarjeta_Cuenta
        Foreign Key (numero_cuenta) References Cuenta  
);
    
CREATE TABLE Producto(
    codigo_producto BIGINT      NOT NULL,
    nombre          VARCHAR     NOT NULL,
    precio          FLOAT       NOT NULL,
    stock           INT         NOT NULL,
    qr              CHAR ,     
    CONSTRAINT  PKProducto
        Primary Key (codigo_producto)
);

CREATE TABLE Pedido_Compuesto(
    id              BIGINT      NOT NULL,
    fecha           DATE        NOT NULL,
    canal_de_compra VARCHAR,
    dni_cliente     INT         NOT NULL,
    CONSTRAINT PKPedido_Compuesto
        Primary Key (id),
    CONSTRAINT FKPedido_Compuesto_Cliente
        Foreign Key (dni_cliente) References Cliente(dni)
);


CREATE TABLE Pedido_Simple(
    id              BIGINT      NOT NULL,
    precio_total    FLOAT       NOT NULL,
    estado          VARCHAR     NOT NULL,
    fecha           DATE        NOT NULL,
    canal_de_compra VARCHAR,
    nro_pedido_compuesto    BIGINT  NOT NULL,
    dni_cliente     INT         NOT NULL,
    CONSTRAINT PKPedido_Simple
        Primary Key (id),
    CONSTRAINT FKPedido_Simple_Pedido_Compuesto
        Foreign Key (nro_pedido_compuesto) References Pedido_Compuesto(id),
    CONSTRAINT FKPedido_Simple_Cliente
        Foreign Key (dni_cliente) References Cliente(dni)
);

CREATE TABLE Producto_Pedido(
    codigo_producto BIGINT      NOT NULL,
    id_pedido_simple BIGINT     NOT NULL,
    cantidad        INT         NOT NULL,
    CONSTRAINT PKProducto_Pedido
        Primary Key (codigo_producto, id_pedido_simple),
    CONSTRAINT FKProducto_Pedido_Pedido_Simple
        Foreign Key (id_pedido_simple) References Pedido_Simple(id),
    CONSTRAINT FKProducto_Pedido_Producto
        Foreign Key (codigo_producto) References Producto(codigo_producto)
);

CREATE TABLE Cobro(
    id_pedido       BIGINT      NOT NULL,
    numero_cuenta   BIGINT      NOT NULL,
    aprobado        BOOLEAN     NOT NULL,
    nro_aprobacion  BIGINT,
    CONSTRAINT PKCobro
        Primary Key (id_pedido),
    CONSTRAINT FKCobro_Pedido_Simple
        Foreign Key (id_pedido) References Pedido_Simple(id),
    CONSTRAINT FKCobro_Cuenta
        Foreign Key (numero_cuenta) References Cuenta(numero_cuenta)
);