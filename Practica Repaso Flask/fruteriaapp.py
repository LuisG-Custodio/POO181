from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app= Flask(__name__)
#conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DB_Fruteria'
app.secret_key= 'mysecretkey'
mysql= MySQL(app)

@app.route('/')
def index():
    CC= mysql.connection.cursor()
    CC.execute('select * from tbFrutas')
    regFrutas= CC.fetchall()
    return render_template('index.html',listaFrutas = regFrutas)

@app.route('/ingresofruta')
def ingresofruta():
    return render_template('ingreso_fruta.html')

@app.route('/guardarfruta', methods=['POST'])
def guardarfruta():
    if request.method == 'POST':
        Vfruta=request.form['txtFruta']
        Vtemporada=request.form['txtTemporada']
        Vprecio=request.form['txtPrecio']
        Vstock=request.form['txtStock']
        CC= mysql.connection.cursor()
        CC.execute('insert into tbFrutas(fruta, temporada, precio, stock) values(%s,%s,%s,%s)',(Vfruta,Vtemporada,Vprecio,Vstock))
        mysql.connection.commit()           
    flash('La fruta fue agregada correctamente')
    return redirect(url_for('index'))

@app.route('/editarfruta/<id>')
def editarfruta(id):
    CC= mysql.connection.cursor()
    CC.execute('select * from tbFrutas where id=%s',(id,))
    regFruta= CC.fetchone()
    return render_template('editar_frutas.html',Fruta = regFruta)

@app.route('/actualizarfruta/<id>', methods=['POST'])
def actualizarfruta(id):
    if request.method == 'POST':
        Vfruta=request.form['txtFruta']
        Vtemporada=request.form['txtTemporada']
        Vprecio=request.form['txtPrecio']
        Vstock=request.form['txtStock']
        CC= mysql.connection.cursor()
        CC.execute('update tbFrutas set fruta=%s, temporada=%s, precio=%s, stock=%s where id=%s',(Vfruta,Vtemporada,Vprecio,Vstock,id,))
        mysql.connection.commit()           
    flash('Los datos de la fruta '+ Vfruta +' fueron actualizados correctamente')
    return redirect(url_for('index'))
    

@app.route('/borrarfruta/<id>')
def eliminar(id):
    CC= mysql.connection.cursor()
    CC.execute('select * from tbFrutas where id=%s',(id,))
    regFruta= CC.fetchone()
    return render_template('borrar_frutas.html',Fruta = regFruta)

@app.route('/eliminarfruta/<id>', methods=['POST'])
def borrado(id):
    if request.method == 'POST':
        CC= mysql.connection.cursor()
        CC.execute('delete from tbFrutas where id=%s',(id,))
        mysql.connection.commit()           
    flash('Los datos de la fruta fueron eliminados correctamente')
    return redirect(url_for('index'))

@app.route('/busquedafruta/<id>')
def busquedafruta(id):
    CC= mysql.connection.cursor()
    CC.execute('select id,fruta from tbFrutas')
    idFrutas= CC.fetchall()
    CC.execute('select * from tbFrutas where id=%s',(id,))
    regFruta= CC.fetchone()
    return render_template('busqueda_fruta.html',listaFrutas = idFrutas,Fruta = regFruta)

@app.route('/realizarbusqueda', methods=['POST'])
def realizarbusqueda():
    if request.method == 'POST':
        Vid=request.form["txtId"]   
    return redirect('busquedafruta/'+Vid)

        

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)