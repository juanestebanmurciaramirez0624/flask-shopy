from flask import render_template
from . import productos
import app
from .forms import RegistrarProductoForm
import os

#rutas del modulo productos "productos"
@productos.route("/listar")
def listar():
    # definir el formulario
    form = RegistrarProductoForm()
    # listar los productos utilizando 
    # modelos
    productos = app.models.Producto.query.all()
    return render_template("listaCliente.html",
                           productos =  productos)



@productos.route("/nuevo",
                 methods=["GET", "POST"])
def nuevo():
     # definir el formulario
    form = RegistrarProductoForm()
    #definir el objeto producto vacio
    p= app.models.Producto()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #return os.getcwd()
        #Extraer el objeto FileStorage
        file = form.imagen.data
        file.save(os.path.abspath(os.getcwd() + 
                                  "/app/productos/imagenes/" + form.imagen.data.filename))
        return "Producto registrado mi amor ♥"

    return render_template("registrar_producto.html",
                           form = form)