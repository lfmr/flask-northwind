from crypt import methods

from flask import render_template, request, redirect
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    cursor = db.get_db().cursor()
    # Obtiene los empleados
    cursor.execute("""select * from employees""")
    empleados = [dict((cursor.description[i][0], value)
                      for i, value in enumerate(row))
                 for row in cursor.fetchall()]

    # Obtiene los clientes
    cursor.execute("""select * from customers order by company""")
    clientes = [dict((cursor.description[i][0], value)
                     for i, value in enumerate(row))
                for row in cursor.fetchall()]

    # Obtiene las ordenes
    where = " 1=1 "
    ordenID = request.args.get('id')
    customer_id = request.args.get('customer_id')
    employee_id = request.args.get('employee_id')

    if ordenID is not None and ordenID != '':
        where += """ and orders.id = {}""".format(ordenID)
    if customer_id is not None and customer_id != '':
        where += """ and orders.customer_id = {}""".format(customer_id)
    if employee_id is not None and employee_id != '':
        where += """ and orders.employee_id = {}""".format(employee_id)
    query = """select orders.*, 
        CONCAT(customers.last_name, ' ', customers.first_name) as customer_name,
        CONCAT(employees.last_name, ' ', employees.first_name) as employee_name
    from orders
    inner join customers on customers.id = orders.customer_id   
    inner join employees on employees.id = orders.employee_id   
    where {} order by id""".format(where)

    cursor.execute(query)
    ordenes = [dict((cursor.description[i][0], value)
                     for i, value in enumerate(row))
                for row in cursor.fetchall()]

    return render_template("index.html", empleados=empleados, clientes=clientes, ordenes=ordenes)


@app.route('/orden/<id>/')
def ver_orden(id):
    cursor = db.get_db().cursor()

    # Obtiene los empleados
    cursor.execute("""select * from employees""")
    empleados = [dict((cursor.description[i][0], value)
                      for i, value in enumerate(row))
                 for row in cursor.fetchall()]

    # Obtiene los clientes
    cursor.execute("""select * from customers order by company""")
    clientes = [dict((cursor.description[i][0], value)
                     for i, value in enumerate(row))
                for row in cursor.fetchall()]

    cursor.execute("""select * from orders where id = %s """, id)
    orden = [dict((cursor.description[i][0], value)
                     for i, value in enumerate(row))
                for row in cursor.fetchall()][0]

    return render_template("orden.html", empleados=empleados, clientes=clientes, id=id, orden=orden)

@app.route("/orden/<id>/eliminar")
def eliminar_orden(id):
    cursor = db.get_db().cursor()
    cursor.execute("""delete from invoices where order_id = %s""", id)
    cursor.execute("""delete from order_details where order_id = %s""", id)
    cursor.execute("""delete from orders where id = %s""", id)
    db.get_db().commit()
    return redirect("/")


@app.route("/orden/<id>/modificar", methods=['POST'])
def modificar_orden(id):
    print(request.form['ship_name'])
    return redirect("/")
