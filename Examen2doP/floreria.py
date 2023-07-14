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


if __name__ == '__main__':
    app.run(port=5000, debug=True)