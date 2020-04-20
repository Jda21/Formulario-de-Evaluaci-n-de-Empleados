from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'John_20'
app.config['MYSQL_DB'] = 'flaskformulario'
mysql = MySQL(app)

# settings
app.secret_key ='mysecretkey'

# cambios para la tabla
@app.route('/')
def Index():
      cur = mysql.connection.cursor()
      cur.execute('SELECT * FROM eval')
      data = cur.fetchall()
      return render_template('index.html', eval = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
        num4 = request.form['num4']
        num5 = request.form['num5']
        num6 = request.form['num6']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO eval (fullname, phone, email, num1, num2, num3, num4, num5, num6) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (fullname, phone, email, num1, num2, num3, num4, num5, num6))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))
  

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM eval WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit-for.html', contact = data[0])


@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        num1 = request.form['num1']
        num2 = request.form['num2']
        num3 = request.form['num3']
        num4 = request.form['num4']
        num5 = request.form['num5']
        num6 = request.form['num6']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE eval
            SET fullname = %s,
                email = %s,
                phone = %s,
                num1 = %s,
                num2 = %s,
                num3 = %s,
                num4 = %s,
                num5 = %s,
                num6 = %s
            WHERE id = %s
        """, (fullname, email, phone, num1, num2, num3, num4, num5, num6, id))
        flash('Edision Exitosa')
        mysql.connection.commit()
        return redirect(url_for('Index'))  




@app.route('/delete/<string:id>')
def delete_contact(id):
  cur = mysql.connection.cursor()
  cur.execute('DELETE from eval WHERE id = {0}'. format(id))
  mysql.connection.commit()
  flash('Contacto Eliminado')
  return redirect(url_for('Index'))

if __name__ == '__main__':
 app.run(port = 3000, debug = True)
