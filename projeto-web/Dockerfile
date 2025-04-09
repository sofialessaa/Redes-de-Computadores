# Usa uma imagem base do Python
FROM python:3.9-slim

# Cria uma pasta para a aplicação
WORKDIR /app

# Copia o arquivo de dependências para dentro do contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto dos arquivos do projeto
COPY . .

# Expõe a porta onde a aplicação vai rodar (exemplo: 5000)
EXPOSE 5000

# Comando de execução
CMD ["python", "app.py"]