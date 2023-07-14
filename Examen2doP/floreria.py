from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app= Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_floreria'
app.secret_key= 'mysecretkey'
mysql= MySQL(app)

@app.route('/')
def index():
    CC= mysql.connection.cursor()
    CC.execute('select * from tbflores')
    listaflores=CC.fetchall()
    return render_template('index.html', flores=listaflores)

@app.route('/insertarflor')
def insertarflor():
    return render_template('inserrtarflor.html')

@app.route('/guardarflor', methods=['POST'])
def guardarflor():
    if request.method == 'POST':
        Vnombre=request.form['txtNombre']
        Vcantidad=request.form['txtCantidad']
        Vprecio=request.form['txtPrecio']
        CC= mysql.connection.cursor()
        CC.execute('insert into tbflores(nombre,cantidad,precio) values (%s,%s,%s)',(Vnombre,Vcantidad,Vprecio))
        mysql.connection.commit()           
    flash('Los datos de la flor fueron agregados correctamente')
    return redirect(url_for('index'))


@app.route('/buscarflor/<nom>')
def buscarflor(nom):
    CC= mysql.connection.cursor()
    CC.execute('select * from tbflores where id=%s',(nom))
    flores=CC.fetchone()
    return render_template('buscar_flor.html',flor=flores)
    
    
@app.route('/buscadorflor', methods=['POST'])
def buscadorflor():
    if request.method == 'POST':
        Vnombre=request.form['txtNombre']
        CC= mysql.connection.cursor()
        CC.execute('select id from tbflores where nombre = %s',(Vnombre))
        id=CC.fetchone()     
    return redirect('/buscarflor/'+id)

@app.route('/editarflor/<nom>')
def editarflor(nom):
    CC= mysql.connection.cursor()
    CC.execute('select * from tbFlores where id=%s',(nom))
    regFlor= CC.fetchone()
    return render_template('editarflor.html',Flor = regFlor)

@app.route('/actualizarflor/<id>', methods=['POST'])
def actualizarflor(id):
    if request.method == 'POST':
        Vnombre=request.form['txtNombre']
        Vcantidad=request.form['txtCantidad']
        Vprecio=request.form['txtPrecio']
        CC= mysql.connection.cursor()
        CC.execute('update tbFlores set nombre=%s, cantidad=%s, precio=%s where id=%s',(Vnombre,Vcantidad,Vprecio,id,))
        mysql.connection.commit()           
    flash('Los datos de la flor fueron actualizados correctamente')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)