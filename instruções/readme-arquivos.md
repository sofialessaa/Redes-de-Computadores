## Passo a passo para criar a estrutura de diretórios e arquivos no seu terminal

### Estrutura do Projeto
```
Redes-de-Computadores/
│
├── docker-compose.yml
├── nginx/
│   └── default.conf
├── projeto-web/
│   └── Dockerfile
│   └── app.py
|   └── static/
|   └── templates/
|   └── requirements.txt
|   └── bdaws.txt
|   └── .gitignore
```
---

### • Passo 1: Criar pasta do projeto
```bash
sudo mkdir projeto-web
cd projeto-web
```
---

### • Passo 2: Criar arquivo app.py 
```bash
sudo nano app.py
```
<details>
  <summary>Conteudo app.py</summary>
  
```bash
# Importa as bibliotecas necessárias
from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
import os

# Cria a aplicação Flask
app = Flask(__name__)

# Captura o nome do servidor enviado pela variável de ambiente (usado para mostrar qual container respondeu)
server_name = os.environ.get("SERVER_NAME", "Default Server")

# Configurações de conexão com o banco de dados MySQL hospedado na AWS RDS
app.config['MYSQL_HOST'] = 'database-1.cyuqerkjhmh8.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'ProjetoRedes'  # Atenção: nunca compartilhe senhas reais em repositórios públicos!
app.config['MYSQL_DB'] = 'bdaws'

# Inicializa o MySQL com as configurações acima
mysql = MySQL(app)

# Rota principal para cadastro de usuários
@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        # Coleta os dados enviados pelo formulário
        nome = request.form['nome']
        email = request.form['email']
        filme = request.form['filme']
        nota = request.form['nota']
        opiniao = request.form['opiniao']

        # Insere os dados no banco de dados
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios(nome, email, filme, nota, opiniao) VALUES (%s, %s, %s, %s, %s)", 
                    (nome, email, filme, nota, opiniao))
        mysql.connection.commit()
        cur.close()

        # Recarrega a página após o cadastro
        return render_template('cadastro.html')
    
    # Renderiza o formulário se for GET
    return render_template('cadastro.html')

# Rota para editar um cadastro existente
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

        # Redireciona para a página de listagem após salvar
        return redirect(url_for('users'))
    
    # Busca os dados do usuário no banco para preencher o formulário
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    user = cur.fetchone()
    cur.close()
    return render_template('editar.html', user=user)

# Rota para excluir um usuário
@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('users'))

# Rota para listar todos os usuários cadastrados
@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM usuarios")

    if users > 0:
        userDetails = cur.fetchall()  # Pega todos os registros
        return render_template("users.html", userDetails=userDetails)
    
    # Caso não haja nenhum registro
    return 'Nenhum usuário encontrado.'

# Torna o nome do servidor acessível nos templates HTML
@app.context_processor
def inject_server_name():
    return dict(server_name=server_name)

# Roda a aplicação Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
</details>

---

### • Passo 3: Criar requirements.txt
```bash
sudo nano requirements.txt
```

<details>
  <summary>Conteúdo de requirements.txt</summary>
  
``` bash
blinker==1.9.0 #Utilitário de sinais usado internamente pelo Flask
click==8.1.8 #Biblioteca para criação de comandos de linha de comando (CLI), usada pelo Flask
colorama==0.4.6 #Fornece suporte a cores no terminal, útil em ambientes Windows
Flask==3.1.0 #Microframework web principal utilizado no projeto
itsdangerous==2.2.0 #Fornece funções para segurança, como geração de tokens, usado internamente no Flask
Jinja2==3.1.6 #Template engine utilizada pelo Flask para renderizar HTML
MarkupSafe==3.0.2 #Dependência do Jinja2, usada para manipulação segura de strings HTML 
Werkzeug==3.1.3 #Ferramenta WSGI que gerencia requisições/respostas HTTP no Flask
Flask-MySQLdb==2.0.0 #Extensão do Flask para integração com bancos de dados MySQL
```
</details>

---

### • Passo 4: Criar Dockerfile
```bash
sudo nano Dockerfile
```
<details> 
  <summary>Conteúdo de Dockerfile</summary>
  
```bash
# Usa uma imagem leve do Python baseada no Debian Bookworm
FROM python:3.9-slim-bookworm

# Atualiza os pacotes do sistema e instala dependências necessárias para compilar e conectar ao MySQL
RUN apt-get update && apt-get install -y \
    build-essential \                   # Ferramentas para compilar pacotes Python com código C/C++
    default-libmysqlclient-dev \       # Biblioteca necessária para conectar com MySQL (ex: mysqlclient)
    pkg-config \                        # Utilitário que ajuda na compilação de pacotes nativos
    && rm -rf /var/lib/apt/lists/*     # Limpa o cache do APT para reduzir o tamanho final da imagem

# Define o diretório de trabalho dentro do container (tudo será executado a partir daqui)
WORKDIR /app

# Copia primeiro o arquivo requirements.txt para instalar as dependências (boa prática de cache)
COPY requirements.txt .

# Instala as bibliotecas Python necessárias para o projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação (app.py, templates, etc.) para o container
COPY . .

# Expõe a porta 5000, que é onde o Flask roda por padrão
EXPOSE 5000

# Comando que será executado ao iniciar o container (roda o app Flask)
CMD ["python", "app.py"]
```  
</details>

---

### • Passo 5: Configurar NGINX como Proxy Reverso e Load Balancer
* Voltar para pasta raiz e criar pasta nginx
```bash
cd ..
sudo mkdir nginx
cd nginx
sudo nano default.conf
```
<details> 
  <summary>Conteúdo de default.conf</summary>
  
``` bash
# Define o grupo de servidores (backend) para balanceamento de carga
upstream backend {
        server app1:5000 weight=3;  # O container app1 tem mais peso (será escolhido com mais frequência)
        server app2:5000 weight=1;  # app2 e app3 têm menos peso, usados com menos frequência
        server app3:5000 weight=1;
}

# Configuração do servidor NGINX que escuta na porta 80
server {
        listen 80;  # Porta padrão para requisições HTTP

        location / {
                proxy_pass http://backend; # Redireciona as requisições para o grupo de servidores definido acima
                proxy_set_header Host $host; # Encaminha o nome do host original (opcional, mas pode ser útil para logs)
                proxy_set_header X-Real-IP $remote_addr; # Encaminha o IP real do cliente que fez a requisição
        }
}

```  
</details>

---

### • Passo 6: Criar docker-compose.yml na raiz do projeto
* Voltar para pasta raiz
```bash
cd ..
sudo nano docker-compose.yml
```

<details>
  <summary>Conteúdo de docker-compose.yml</summary>
  
```bash
version: '3.8'  # Define a versão do Docker Compose

services:  # Seção onde definimos os serviços (containers)

  # Primeiro container da aplicação
  app1:
    build: ./projeto-web            # Caminho para o Dockerfile da aplicação
    container_name: app1            # Nome do container no Docker (facilita identificar)
    environment:
      SERVER_NAME: "Servidor 1"     # Variável de ambiente que será usada na aplicação Flask
    ports:
      - "5001:5000"                 # Porta externa 5001 → porta interna 5000

  # Segundo container da aplicação
  app2:
    build: ./projeto-web
    container_name: app2
    environment:
      SERVER_NAME: "Servidor 2"
    ports:
      - "5002:5000"

  # Terceiro container da aplicação
  app3:
    build: ./projeto-web
    container_name: app3
    environment:
      SERVER_NAME: "Servidor 3"
    ports:
      - "5003:5000"

  # Container do NGINX atuando como proxy reverso e balanceador de carga
  nginx:
    image: nginx:latest             # Usa a imagem mais recente do NGINX
    container_name: loadbalancer    # Nome do container do NGINX
    depends_on:
      - app1
      - app2
      - app3                        # Garante que o NGINX só suba após os apps
    ports:
      - "80:80"                     # Porta 80 do host → porta 80 do container (HTTP padrão)
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
        # Monta o arquivo de configuração do NGINX no container
        # :ro = read-only (protege contra alterações acidentais)

```
</details>

---

### Passo 7: Acesse o seu repositório (pasta) e instale o Docker + Docker Compose
``` bash
cd <nome-da-pasta> #No nosso caso é o nome do repositório!
```
``` bash
sudo apt install docker-compose docker.io -y  
```
* Rodar a aplicação
``` bash
sudo docker-compose up --build -d
```
---

### Alguns comandos para o docker:
``` bash
sudo docker ps #verifique se os conteiners estão rodando
```
``` bash
sudo docker logs <nome-do-container> #veja os logs de algum container
```
``` bash
sudo docker-compose down #encerre e remova todos os containers
```
