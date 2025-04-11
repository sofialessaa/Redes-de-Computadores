## 🧱 Passo a Passo Completo da Infraestrutura (EC2, Docker, NGINX)

### Passo 1: Acesse sua AWS e crie uma instância!
* Vá em **Executar Instâncias**, de um nome a ela e escolha Ubuntu!

![image](https://github.com/user-attachments/assets/b94b563b-196c-48b2-94ba-39641e4a5df8)

<img align="center" src="https://github.com/user-attachments/assets/c5929751-9e10-4a51-a95a-1a741a23e024" width="500">

* Selecione uma chave ou crie uma nova.

  <img src="https://github.com/user-attachments/assets/e6deabac-1aed-47f4-8e4a-86e0ab3085e2" width="500"> 
  
  <img src="https://github.com/user-attachments/assets/83c8adfa-8e46-4129-8b61-fed04c7389ce" width="500">

* Em **Configurações de rede** selecione essas opções:

 ![image](https://github.com/user-attachments/assets/af146aa2-52e2-4d54-a540-aa97ace5dea3)

---

### Passo 2: Configurar as portas no Grupo de Segurança
![image](https://github.com/user-attachments/assets/382b3165-b079-454f-8e99-c26e5f0cdcbd)
![image](https://github.com/user-attachments/assets/63fb2003-82f6-451e-9bb7-4a5587e84106)

* Clique em **Editar regras de entradas** e adicione as portas: 3306 (Mysql) e 5000-5005. No meu caso eu também adicionei a porta 8080, caso precisasse ja teria.

![image](https://github.com/user-attachments/assets/c2915104-9dc3-4ebb-893c-72b94edd0e98)

---

### Passo 3: Conectando no Terminal da sua máquina
* Copie o seu Endereço IPv4 público e no terminal escreva:
  
``` bash
cd Downloads
```
``` bash
ssh -i <nome-da-chave>.pem ubuntu@<ip> #Não esqueça de tirar os <> e só substituir.
```
---

### Passo 4: Configurar o DOCKER
* Atualizar a instância  
``` bash
sudo apt update
```
``` bash
sudo apt upgrade -y
```
* Clone o seu repositório ou crie as pastas e arquivos no terminal
    * Quer criar as pastas pelo terminal? [Acesse Aqui](./instruções/readme-arquivos.md)
``` bash
git clone <url-do-repositorio> #Comando para clonar o repositório do GitHub
```
* Acesse o seu repositório (pasta) e instale o Docker + Docker Compose
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

