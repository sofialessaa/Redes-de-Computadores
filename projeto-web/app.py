from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

server_name = os.environ.get("SERVER_NAME", "Default Server")

# Conexão com o banco de dados
app.config['MYSQL_HOST'] = 'database.cbqfmw47p9tq.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'atvRedes2025' #SENHA AQUI
app.config['MYSQL_DB'] = 'bdaws'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        filme = request.form['filme']
        nota = request.form['nota']
        opiniao = request.form['opiniao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios(nome, email, filme, nota, opiniao) VALUES (%s, %s, %s, %s, %s)", (nome, email, filme, nota, opiniao))
        mysql.connection.commit()
        cur.close()
        return render_template('cadastro.html')
    return render_template('cadastro.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        # Atualiza os dados do usuário no banco
        nome = request.form['nome']
        email = request.form['email']
        filme = request.form['filme']
        nota = request.form['nota']
        opiniao = request.form['opiniao']

        cur.execute("""
            UPDATE usuarios 
            SET nome=%s, email=%s, filme=%s, nota=%s, opiniao=%s 
            WHERE id=%s
        """, (nome, email, filme, nota, opiniao, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('users'))
    
    # Busca os dados atuais do usuário para preencher o formulário de edição
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    user = cur.fetchone()
    cur.close()
    return render_template('editar.html', user=user)

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('users'))

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM usuarios")

    if users > 0:
        userDetails = cur.fetchall()
        return render_template("users.html", userDetails=userDetails)
    return 'Nenhum usuário encontrado.'

@app.context_processor
def inject_server_name():
    return dict(server_name=server_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
