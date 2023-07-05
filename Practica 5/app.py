#importación del framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#inicialización del APP
app= Flask(__name__)
#conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
app.secret_key= 'mysecretkey'
mysql= MySQL(app)

#declaración de ruta / http://localhost:5000
@app.route('/')
def index():
    CC= mysql.connection.cursor()
    CC.execute('select * from tb_albums')
    conAlbums= CC.fetchall()
    print(conAlbums)
    return render_template('index.html',listAlbums = conAlbums)

# ruta / http://localhost:5000/guardar | tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        #pasamos a variables el contendio de los input
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        
        #Conectar y ejecutar el insert
        CS= mysql.connection.cursor()
        CS.execute('insert into tb_albums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()           
    flash('Los datos del album fueron agregados correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    CC= mysql.connection.cursor()
    CC.execute('select * from tb_albums where id=%s',(id,))
    consulId= CC.fetchone()
    return render_template('editarAlbum.html',album = consulId)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        CS= mysql.connection.cursor()
        CS.execute('update tb_albums set titulo=%s,artista=%s,anio=%s where id=%s',(Vtitulo,Vartista,Vanio,id))
        mysql.connection.commit()           
    flash('Los datos del album '+ Vtitulo +' fueron actualizados correctamente')
    return redirect(url_for('index'))
    

@app.route('/eliminar/<id>')
def eliminar(id):
    CC= mysql.connection.cursor()
    CC.execute('select * from tb_albums where id=%s',(id,))
    consulId= CC.fetchone()
    return render_template('eliminarAlbum.html',album = consulId)

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)