""" Importación del Framework """
from flask import Flask, render_template, request, redirect, url_for, flash

""" Importación de MySQL """
from flask_mysqldb import MySQL

""" Inicialización del APP """
app= Flask(__name__)

""" Configuración de la conexión """
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DBFlask'
app.secret_key='mysecretkey'
mysql=MySQL(app)

""" Declaración de la ruta, pertenece a http://localhost:5000  (El @app.route('/') es la ruta index o ruta principal)"""
@app.route('/') 
def index():
    return render_template('index.html')

""" Ruta http:localhost:5000/guardar tipo POST para Insert """
""" "Methods" La ruta va a recibir información del formulario """
@app.route('/guardar', methods=['POST']) 
def Guardar():
    if request.method == 'POST':

        """ Pasamos a variables el contenido de los imputs """
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
      
        """ Conectar a la BD y ejecutar el insert """
        CS= mysql.connection.cursor()
        CS.execute('insert into tb_albums(titulo, artista, anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
        
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar') 
def Eliminar():
    return "Se eliminó en la BD"

""" Ejecución del servidor a través del puerto 5000 """
if __name__ == '__main__':
    app.run(port=5000,debug=True)
