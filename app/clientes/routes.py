from flask import render_template
from . import clientes
import app
from .form import RegistrarClientesForm
import os

#rutas del modulo clientes "clientes"
@clientes.route("/listar")
def listar():
    # definir el formulario
    form = RegistrarClientesForm()
    # listar los clientes utilizando 
    # modelos
    clientes = app.models.Cliente.query.all()
    return render_template("index.html",
                           clientes =  clientes)



@clientes.route("/nuevo",
                 methods=["GET", "POST"])
def nuevo():
     # definir el formulario
    form = RegistrarClientesForm()
    #definir el objeto cliente vacio
    c = app.models.Cliente()
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        return "Cliente registrado mi amor ♥"

    return render_template("registrar_cliente.html",
                           form = form)