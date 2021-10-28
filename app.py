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
    User= Datos_Usuario.select().where(Datos_Usuario.email ==user).tuples()
    cargo=[filas[8] for filas in User]
    if "Superadministrador" in cargo:
        rango="Superadministrador" 
        return render_template("layout.html", rango=rango)
    elif "Administrador" in cargo:
        rango="Administrador"
        return render_template("layout.html", rango = rango)
    elif "Usuario" in cargo:
        rango="Usuario"
        return render_template("layout.html", rango = rango)
    else:
        return render_template(".html")
        

@app.route("/logout",methods=['GET','POST'])
def logout():
    logout_user()
    return render_template('home.html')

@app.route('/')
def index():   
    return render_template("home.html")


@app.route("/login", methods=["GET","POST"])

def login():
    Dato_inicial()
    if request.method=='POST':
        userid= request.values['username']
        password= request.values['password']  
        bd = Datos_Usuario.select().tuples()
        user=[filas[5] for filas in bd]
        contraseñas=[filas[9] for filas in bd]
        

        if  userid in user and password in contraseñas:
            
            return user_loader(userid)
        else:
            return   render_template('home.html') #usuario=userid, clave=password) 
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
        clave=request.form.get('clave')
        try:   
            ingresar_datos_usuario(nombre,apellido,genero,documento,direccion,email,telefono,cel,cargo,clave)
        except peewee.IntegrityError:
            error=True
            return render_template("crearAdmin.html", rango=rango, error=error)
            
    return render_template("crearAdmin.html", rango=rango)


# ***************BUSCAR USUARIO GENERAL***************

# BUSCARA USUARIO
@app.route("/buscarUsuario", methods=["GET", "POST"])
def buscarAdmin():
    
    if 'buscar' in request.values:
        doc_bus=request.form.get('doc_buscar')        
        print(doc_bus)
        datos=select_U(doc_bus)
        return render_template("buscarUsuario.html", datos=datos, rango=rango)
            
    
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
        return render_template("buscarUsuario.html", datos=datos, rango=rango)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('documento')
        delete_U(doc_elim)
        return render_template("buscarUsuario.html", rango=rango)
    else:
        return render_template("buscarUsuario.html", rango=rango)

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
            return render_template('crearProv.html', rango=rango, error=error)
    return render_template('crearProv.html', rango=rango)

# BUSCARA PROVEEDOR
@app.route("/buscarProv", methods=["GET", "POST"])
def buscarProv():
    
    if 'buscar' in request.values:
        nit_bus=request.form.get('nit_bus')
        datos=select_Prov(nit_bus)
        return render_template("buscarProv.html", datos=datos, rango=rango)
            
    
    if 'editar' in request.values:
        nombre=request.form.get('nombre')
        nit=request.form.get('nit')
        direccion=request.form.get('direccion')
        email=request.form.get('email')
        telefono=request.form.get('telefono')
        celular=request.form.get('cel')

        edit_Prov(nombre, nit, direccion, email, telefono, celular)
        datos=select_Prov(nit)

        return render_template("buscarProv.html", datos=datos, rango=rango)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('nit')
        delete_Prov(doc_elim)
        return render_template("buscarProv.html", rango=rango)
    else:
        return render_template("buscarProv.html", rango=rango)



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
        try:
            ingresar_datos_producto(marca,nombre,codigo,color,procesador)
        except peewee.IntegrityError:
            error=False
            return render_template('crearProduc.html', rango=rango, error=error)
    return render_template('crearProduc.html', rango=rango)

# BUSCARA PRODUCTO
@app.route("/buscarProduc", methods=["GET", "POST"])
def buscarProduc():
    
    if 'buscar' in request.values:
        cod_bus=request.form.get('cod_bus')
        datos=select_P(cod_bus)
        return render_template("buscarProduc.html", datos=datos, rango=rango)
            
    
    if 'editar' in request.values:
        marca=request.form.get('marca')
        nombre=request.form.get('nombre')
        codigo=request.form.get('codigo')
        color=request.form.get('color')
        procesador=request.form.get('procesador')

        edit_P(marca,nombre,codigo,color,procesador)
        datos=select_P(codigo)
        return render_template("buscarProduc.html", datos=datos, rango=rango)
    
    if 'eliminar' in request.values:
        doc_elim=request.form.get('codigo')
        delete_P(doc_elim)
        return render_template("buscarProduc.html", rango=rango)
    else:
        return render_template("buscarProduc.html", rango=rango)

    

if __name__ == '__main__':
    
    app.run()