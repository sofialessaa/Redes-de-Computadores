## Passo a passo do Banco de Dados - RDS 

### Passo 1: Pesquise RDS na AWS e clique em Banco de dados
* Selecione **Criar banco de dados**
![image](https://github.com/user-attachments/assets/24f40b79-e580-459e-8dd9-8820201c3729)

---
### Passo 2: Vamos configurar o Banco
* Selecionei **Criação fácil** e **MySql**
![image](https://github.com/user-attachments/assets/2424950b-61af-4d9f-a872-a9ad825c0675)

* Siga as imagens para configurar seu banco
  ![image](https://github.com/user-attachments/assets/fcbeb1b3-d251-402d-ac68-26aa915ff5d3)
  * Adicione uma senha segura e crie o seu banco!
    ![image](https://github.com/user-attachments/assets/1989c39f-7a8f-43ce-a793-6889eb34f01f)

---

### Passo 3: Selecione o bando e clique em Modificar
![image](https://github.com/user-attachments/assets/7ec4eaa8-7f35-4339-92fb-815eeece0ec1)

* Em **Conectividade** vá em **Configuração adicional** e selecione **Publicamente acessível**
  ![image](https://github.com/user-attachments/assets/18ffe351-e130-43af-873a-eee1ef8e4c31)

---
### Passo 4: Configurar Grupo de Segurança
* Clique no seu banco de dados
  ![image](https://github.com/user-attachments/assets/efe1016f-d105-4179-9fdb-b76140467dc4)
  
* Ao clicar no link do **Grupos de segurança da VPC**, selecione o grupo.
  ![image](https://github.com/user-attachments/assets/3359d48e-c9ec-4a41-84bc-77b29e16c87c)

* Em **Editar regras de segurança**, adicione a do MySql/Aurora
  ![image](https://github.com/user-attachments/assets/30677ea0-7687-4f41-baee-fba576c20d3a)

---

### Agora é so copiar o endpoint e mudar as configurações no seu arquivo app.py!
![image](https://github.com/user-attachments/assets/efe1016f-d105-4179-9fdb-b76140467dc4)

* Não se esqueça de criar o database e tabela no seu mysql workbench.
* [Acesse bdaws.txt](./projeto-web/bdaws.txt)
