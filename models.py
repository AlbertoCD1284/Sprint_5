# flask db create models
# flask db upgrade

from peewee import *
from playhouse.flask_utils import FlaskDB
from werkzeug.security import generate_password_hash


db = FlaskDB()

# CLASE PARA PODER CREAR TABLA ADMINISTRADOR


class Datos_Usuario(db.Model):
    nombre = TextField()
    apellido = TextField()
    genero = TextField()
    documento = TextField(primary_key=True, unique=True, null=True)
    direccion = TextField()
    email = TextField(unique=True)
    telefono = TextField()
    cel = TextField(unique=True)
    cargo=TextField()
    clave=TextField()

    

    
def Dato_inicial():
    User_1= Datos_Usuario.select().tuples()
    cargo=[filas[5]  for filas in User_1]
    if "grupo7@uninorte.edu.co" not in cargo:
       entrada = Datos_Usuario.get_or_create(nombre="Grupo7", apellido="uninorte", genero="masculino",
                                                documento="1220", direccion="Uninorte", email="grupo7@uninorte.edu.co", telefono="123", cel="321", cargo="Superadministrador",clave=generate_password_hash("123",method="sha256"))
# INGRESANDO DATOS A LA TABLA DE DATOS: Datos_Usuario, CON LA FUNCION: ingresar_datos_usuario, DESDE: APP /crearAdmin

def ingresar_datos_usuario(nom, ape, gene, doc, direc, email, tel, cel, cargo, clave):
        entrada = Datos_Usuario.get_or_create(nombre=nom, apellido=ape, genero=gene,
                                                documento=doc, direccion=direc, email=email, telefono=tel, cel=cel, cargo=cargo,clave=clave)

# TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: select_U, RETORNAR LISTA: list(query)
def select_U(doc):           
    query = Datos_Usuario.select().where(Datos_Usuario.documento == doc).dicts()
    return list(query)
    

# EDITAR UN DATO DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: edit_U, DESDE: APP /buscarUsuario
def edit_U(nom, ape, gene, doc, direc, email, tel, cel,cargo,clave):
    update = Datos_Usuario.update(nombre=nom, apellido=ape, genero=gene,
                                documento=doc, direccion=direc, email=email, telefono=tel, cel=cel, cargo=cargo,clave=clave).where(Datos_Usuario.documento == doc).execute()

# ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_Admin, CON LA FUNCION: delete_U, DESDE: APP /buscarUsuario
def delete_U(doc_elim):
    go_delete = Datos_Usuario.delete().where(Datos_Usuario.documento == doc_elim).execute()


# ******************PROVEEDOR*******************

class Datos_Proveedor(db.Model):
    nombre=TextField()
    nit=TextField(primary_key=True, unique=True)
    direccion=TextField()
    email=TextField(unique=True)
    telefono=TextField()
    celular=TextField(unique=True)
    
    

# INGRESANDO DATOS A LA TABLA DE DATOS: Datos_Proveedor, CON LA FUNCION: ingresar_datos_proveedor, DESDE: APP /crearProv
def ingresar_datos_proveedor(nombre, nit, direccion, email, telefono, celular):
        entrada, creado = Datos_Proveedor.get_or_create(nombre=nombre, nit=nit, direccion=direccion,
                                email=email, telefono=telefono, celular=celular)

# TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_Proveedor, CON LA FUNCION: select_Prov, RETORNAR LISTA: list(query)
def select_Prov(doc):
    query = Datos_Proveedor.select().where(Datos_Proveedor.nit == doc).dicts()
    return list(query)

# EDITAR UN DATO DE LA TABLA DE DATOS: Datos_Proveedor, CON LA FUNCION: edit_Prov, DESDE: APP /burcarProv
def edit_Prov(nombre, nit, direccion, email, telefono, celular):
    update = Datos_Proveedor.update(nombre=nombre, nit=nit, direccion=direccion,
                                email=email, telefono=telefono, celular=celular).where(Datos_Proveedor.nit == nit).execute()

# ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_Proveedor, CON LA FUNCION: delete_Prov, DESDE: APP /burcarProv
def delete_Prov(doc_elim):
    go_delete = Datos_Proveedor.delete().where(Datos_Proveedor.nit == doc_elim).execute()


# ********************PRODUCTO******************

class Datos_Producto(db.Model):
    marca=TextField()
    nombre=TextField()
    codigo=TextField(primary_key=True, unique=True)
    color=TextField()
    procesador=TextField()
    stock_Requerido=TextField()
    stock_Actual=TextField()
    nit_proveedor= ForeignKeyField(Datos_Proveedor)

    
    


# INGRESANDO DATOS A LA TABLA DE DATOS: Datos_Producto, CON LA FUNCION: ingresar_datos_producto, DESDE: APP /crearProducto
def ingresar_datos_producto(nombre, marca, codigo, color, procesador,stock_Requerido, stock_Actual,nit_proveedor):
    entrada, creado = Datos_Producto.get_or_create(nombre=nombre, marca=marca, codigo=codigo,
                                color=color, procesador=procesador,stock_Requerido=stock_Requerido,stock_Actual=stock_Actual,nit_proveedor=nit_proveedor)


# TOMAR UNA LINEA DE LA TABLA DE DATOS: Datos_Producto, CON LA FUNCION: select_U, RETORNAR LISTA: list(query)
def select_P(doc):
    query = Datos_Producto.select().where(Datos_Producto.codigo == doc).dicts()
    return list(query)

# EDITAR UN DATO DE LA TABLA DE DATOS: Datos_Producto, CON LA FUNCION: edit_P, DESDE: APP /crearProducto
def edit_P(nombre, marca, codigo, color, procesador,stock_Requerido,stock_Actual,nit_proveedor):
    update = Datos_Producto.update(nombre=nombre, marca=marca, codigo=codigo,
                            color=color, procesador=procesador,stock_Requerido=stock_Requerido,stock_Actual=stock_Actual,nit_proveedor=nit_proveedor).where(Datos_Producto.codigo == codigo).execute()

# ELIMINAR UNA LINEA DE LA TABLA DE DATOS: Datos_Producto, CON LA FUNCION: delete_P, DESDE: APP /buscarUsuario
def delete_P(doc_elim):
    go_delete = Datos_Producto.delete().where(Datos_Producto.codigo == doc_elim).execute()

