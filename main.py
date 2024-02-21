from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_READERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'system'
mysql = MySQL(app)


@app.route('/api/customers/<int:id>')
@cross_origin()
def getCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, first_name, last_name, email, telefono, address FROM customers WHERE id='+ str(id) + ';')
    data = cur.fetchall()
    content = {}
    for row in data:
        content = {'id':row[0],'first_name':row[1],'last_name':row[2], 'email':row[3],'telefono':row[4],'address':row[5]}
    return jsonify(content)

@app.route('/api/customers')
@cross_origin()
def getAllCustomers():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, first_name, last_name, email, telefono, address FROM customers')
    data = cur.fetchall()
    resultado = []
    for row in data:
        content = {'id':row[0],'first_name':row[1],'last_name':row[2], 'email':row[3],'telefono':row[4],'address':row[5]}
        resultado.append(content)
    return jsonify(resultado)

@app.route('/api/customers', methods=['POST'])
@cross_origin()
def saveCustomer():
    if 'id' in request.json:
        updateCustomer()
    else:
        createCustomer()
    return 'Cliente Guardado'


def createCustomer():
    curl = mysql.connection.cursor()
    curl.execute("INSERT INTO `customers` (`id`, `first_name`, `last_name`, `email`, `telefono`, `address`) VALUES (NULL, %s, %s, %s, %s, %s);",
                 (request.json['first_name'], request.json['last_name'], request.json['email'], request.json['telefono'], request.json['address']))
    mysql.connection.commit()
    return 'Cliente Creado'

def updateCustomer():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE `customers` SET `first_name` = %s, `last_name` = %s, `email` = %s, `telefono` = %s, `address` = %s WHERE `customers`.`id` = %s;",
                (request.json['first_name'], request.json['last_name'], request.json['email'], request.json['telefono'], request.json['address'], request.json['id']))
    mysql.connection.commit()
    return 'Cliente Actualizado'

@app.route('/api/customers/<int:id>', methods=['DELETE'])
@cross_origin()
def removeCustomer(id):
    curl = mysql.connection.cursor()
    curl.execute("DELETE FROM customers WHERE `customers`.`id` = " + str(id) + ";")
    mysql.connection.commit()
    return 'Cliente Eliminado'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/static/<path:path>')
@cross_origin()
def publicFiles(path):
    return render_template(path)

if __name__ == '__main__':
    app.run(None, 3000, False)