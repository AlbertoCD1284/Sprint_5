from logging import error
from flask import Flask,redirect,url_for,render_template,request
from flask.helpers import flash
from flask_login import LoginManager,login_user,logout_user,login_required, current_user,UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
from config import dev
import peewee

app=Flask(__name__)
app.config.from_object(dev)



db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'


@login_manager.user_loader 
def user_loader(user):
    global rango
    global Datos_U
    User= Datos_Usuario.select().where(Datos_Usuario.email ==user).tuples()
    Datos_U=Datos_Producto.select().tuples()
    cargo=[filas[8] for filas in User]
    if "Superadministrador" in cargo:
        rango="Superadministrador" 
        return render_template("layout.html", rango=rango, Datos_U=Datos_U)
    elif "Administrador" in cargo:
        rango="Administrador"
        return render_template("layout.html", rango = rango,Datos_U=Datos_U)
    elif "Usuario" in cargo:
        rango="Usuario"
        return render_template("layout.html", rango = rango,Datos_U=Datos_U)
    else:
        return render_template("home.html")
        

@app.route("/logout",methods=['GET','POST'])
def logout():
    logout_user()
    return render_template('home.html')

@app.route('/')
def index():   
    Dato_inicial()
    Dato_pinicial()
    return render_template("home.html")

@app.route("/layout", methods=["GET","POST"])
def layout():
    Datos_U=Datos_Producto.select().tuples()
    return render_template('layout.html', rango=rango, Datos_U=Datos_U)


@app.route("/login", methods=["GET","POST"])

def login():
    errorL=False
    if request.method=='POST':
        userid= Datos_Usuario.select().where(Datos_Usuario.email==request.form["username"]).first()
        if userid and check_password_hash(userid.clave, request.form["password"]):
            userL=request.values["username"]
            return user_loader(userL)
        #password=check_password_hash(request.values['password'])
        # password=request.values['password']
        #bd = Datos_Usuario.select().tuples()
        #user=[filas[5] for filas in bd]
        #contrase??as=[filas[9] for filas in bd]
        

        #if  userid in user and password in contrase??as:
            
            
        else:
            errorL=True
            return   render_template('login.html',errorL=errorL) #usuario=userid, clave=password) 
    else :
        return render_template('login.html')


# ****************ADMINISTRADOR*********************

# CREAR ADMINISTRADOR
@app.route("/crearAdmin", methods=["GET", "POST"])
def crearAdmin():
    error=False
    if 'ingresar' in request.values:
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        genero=request.form.get('genero')
        documento=request.form.get('documento')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        cel=request.form.get('cel')
        cargo=request.form.get('cargo')
        clave=generate_password_hash(request.form.get('clave'),method="sha256")
        try:   
            ingresar_datos_usuario(nombre,apellido,genero,documento,direccion,email,telefono,cel,cargo,clave)
        except peewee.IntegrityError:
            error=True
            return render_template("crearAdmin.html", rango=rango, error=error, Datos_U=Datos_U)
            
    return render_template("crearAdmin.html", rango=rango, Datos_U=Datos_U)


# ***************BUSCAR USUARIO GENERAL***************

# BUSCARA USUARIO
@app.route("/buscarUsuario", methods=["GET", "POST"])
def buscarAdmin():
    
    if 'buscar' in request.values:
        doc_bus=request.form.get('doc_buscar')        
        print(doc_bus)
        datos=select_U(doc_bus)
        return render_template("buscarUsuario.html", datos=datos, rango=rango, Datos_U=Datos_U)
            
    
    if 'editar' in request.values:
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        genero=request.form.get('genero')
        documento=request.form.get('documento')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        cel=request.form.get('cel')
        cargo=request.form.get('cargo')
        clave=request.form.get('clave')

        edit_U(nombre,apellido,genero,documento,direccion,email,telefono,cel,cargo,clave)
        datos=select_U(documento)
        return render_template("buscarUsuario.html", datos=datos, rango=rango, Datos_U=Datos_U)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('documento')
        delete_U(doc_elim)
        return render_template("buscarUsuario.html", rango=rango, Datos_U=Datos_U)
    else:
        return render_template("buscarUsuario.html", rango=rango, Datos_U=Datos_U)

# **************CREEAR PROVEEDOR*****************

@app.route("/crearProv",methods=["GET", "POST"])
def crearProv():
    error=False
    if 'ingresar' in request.values:
        nombre=request.form.get('nombre')
        nit=request.form.get('nit')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        celular=request.form.get('celular')
        try:
            ingresar_datos_proveedor(nombre, nit, direccion, email, telefono, celular)
        except peewee.IntegrityError:
            error=True
            return render_template('crearProv.html', rango=rango, error=error, Datos_U=Datos_U)
    return render_template('crearProv.html', rango=rango, Datos_U=Datos_U)

# BUSCARA PROVEEDOR
@app.route("/buscarProv", methods=["GET", "POST"])
def buscarProv():
    
    if 'buscar' in request.values:
        nit_bus=request.form.get('nit_bus')
        datos=select_Prov(nit_bus)
        return render_template("buscarProv.html", datos=datos, rango=rango, Datos_U=Datos_U)
            
    
    if 'editar' in request.values:
        nombre=request.form.get('nombre')
        nit=request.form.get('nit')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        celular=request.form.get('cel')

        edit_Prov(nombre, nit, direccion, email, telefono, celular)
        datos=select_Prov(nit)

        return render_template("buscarProv.html", datos=datos, rango=rango, Datos_U=Datos_U)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('nit')
        delete_Prov(doc_elim)
        return render_template("buscarProv.html", rango=rango, Datos_U=Datos_U)
    else:
        return render_template("buscarProv.html", rango=rango, Datos_U=Datos_U)



# **************CREAR PRODUCTO*******************


@app.route("/crearProduc",methods=["GET", "POST"])
def crearProduc():
    error=False
    if 'ingresar' in request.values:
        marca=request.form.get('marca')
        nombre=request.form.get('nombre')
        codigo=request.form.get('codigo')
        color=request.form.get('color')
        procesador=request.form.get('procesador')
        stock_Requerido=request.form.get('stock_requerido')
        stock_Actual=request.form.get('stock_actual')
        nit_proveedor=request.form.get('nit_prov')
        try:
            ingresar_datos_producto(marca,nombre,codigo,color,procesador,stock_Requerido, stock_Actual,nit_proveedor)
        except peewee.IntegrityError:
            error=False
            return render_template('crearProduc.html', rango=rango, error=error, Datos_U=Datos_U)
    Datos_U=Datos_Producto.select().tuples()
    return render_template('crearProduc.html', rango=rango, Datos_U=Datos_U)

# BUSCARA PRODUCTO
@app.route("/buscarProduc", methods=["GET", "POST"])
def buscarProduc():
    
    if 'buscar' in request.values:
        cod_bus=request.form.get('cod_bus')
        datos=select_P(cod_bus)
        return render_template("buscarProduc.html", datos=datos, rango=rango, Datos_U=Datos_U)
            
    
    if 'editar' in request.values:
        marca=request.form.get('marca')
        nombre=request.form.get('nombre')
        codigo=request.form.get('codigo')
        color=request.form.get('color')
        procesador=request.form.get('procesador')
        stock_Requerido=request.form.get('stock_requerido')
        stock_Actual=request.form.get('stock_actual')
        nit_proveedor=request.form.get('nit_prov')
        edit_P(marca,nombre,codigo,color,procesador,stock_Requerido, stock_Actual,nit_proveedor)
        datos=select_P(codigo)
        return render_template("buscarProduc.html", datos=datos, rango=rango, Datos_U=Datos_U)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('codigo')
        delete_P(doc_elim)
        return render_template("buscarProduc.html", rango=rango, Datos_U=Datos_U)
    else:
        return render_template("buscarProduc.html", rango=rango, Datos_U=Datos_U)

    

if __name__ == '__main__':
    
    app.run()