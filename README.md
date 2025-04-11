## Trabalho Prático: Infraestrutura de Rede Integrada para a Empresa XPTO

### Objetivo
Este projeto tem como objetivo a criação de uma infraestrutura de TI robusta para a empresa XPTO, integrando tecnologias modernas de rede e computação em nuvem. O foco é desenvolver um ambiente de acesso seguro, alta disponibilidade e gerenciamento eficiente de tráfego e dados, promovendo confiabilidade e eficiência para a organização.

<Details>   
  <Summary>    
    📝 Requisitos:
  </Summary>

</br>

**1. Arquitetura da Rede:** 
Desenhar a topologia da rede;

**2. Configuração do Load Balancer:**
Implementar um Load Balancer com Nginx ou HAProxy, configurar o balanceamento entre, no mínimo, 3 máquinas para distribuir o tráfego, criar um mecanismo de monitoramento de disponibilidade e resposta dos servidores; 

**3. Proxy Reverso:** 
Configurar uma máquina com Nginx para atuar como Proxy Reverso, gerenciar requisições e redirecioná-las para os servidores apropriados;

**4. Banco de Dados:** 
Criar um servidor dedicado para o banco de dados usando Docker ou AWS RDS, escolher entre MySQL, PostgreSQL ou MongoDB e justificar a escolha;

**5. VPN (Virtual Private Network):** 
Configurar uma VPN segura (OpenVPN) para acessos externos e integrar a VPN ao firewall da rede para maior controle de acessos;

**6. Docker e Virtualização:** 
Utilizar Docker para hospedar servidores web e banco de dados, criar um docker-compose para gerenciamento facilitado dos serviços, demonstrar a escalabilidade dos containers e a comunicação entre eles;

**7. Endereçamento IPv4 e Segmentação de Redes:** 
Definir a estrutura de endereçamento da empresa e implementar DHCP para gerenciar alocação dinâmica de endereços.

</Details>

---

###  Arquitetura da rede
![dagrama-de-redes](https://github.com/user-attachments/assets/4d005e48-e671-4976-875d-962a99841b41)

---

### Visão Geral
A aplicação foi construída utilizando Docker, organizada em múltiplos containers. É dividida em três componentes principais: o backend (que executa o servidor Python/Flask), o Nginx (como proxy reverso e balanceador de carga), e o Banco de Dados MySQL hospedado na AWS RDS (para armazenamento de dados relacionados aos usuários e suas opiniões sobre filmes).

---

### Tecnologias utilizadas
![AWS](https://img.shields.io/badge/aws-232F3E.svg?style=for-the-badge&logo=aws&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Docker](https://img.shields.io/badge/docker-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![AWS RDS](https://img.shields.io/badge/AWS_RDS-527FFF.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

---

<Details> 
  <Summary>
    🏗️ Estrutura do Projeto
  </Summary>

</br>

O projeto está dividido em:

- **Backend (Flask)**: Três servidores, cada um executando a mesma aplicação, mas distribuídos para melhorar a escalabilidade e o balanceamento de carga;
- **NGINX**: Atua como um proxy reverso e balanceador de carga, distribuindo as requisições entre os três servidores (app1, app2, app3);
- **Docker Compose**: Orquestra os containers e redes;
- **Banco de Dados (MySQL na AWS)**:  Armazena as informações dos usuários e suas interações com a aplicação (como suas avaliações de filmes);
- **RDS da AWS**: Oferece segurança, escalabilidade e gerenciamento automatizado.

</Details> 

<Details> 
  <Summary>
    🧠 Arquitetura e Justificativa Técnica
  </Summary>

#### 1. Uso do Docker
Permite isolar os componentes da aplicação - backend e proxy - em containers separados. Isso oferece vantagens:

- Isolamento e Independência: Cada parte funciona de forma independente, o que facilita a manutenção e a atualização de componentes sem afetar o funcionamento dos outros;
- Escalabilidade: Com o Docker, é fácil escalar a aplicação para mais servidores, conforme necessário. Por exemplo, podemos adicionar mais containers appX sem alterar a configuração de outros serviços;
- Portabilidade: A aplicação é executada no mesmo ambiente em qualquer máquina ou servidor, garantindo consistência entre desenvolvimento, testes e produção.

#### 2. Balanceamento de Carga com NGINX
Estamos usando o Nginx como proxy reverso e load balancer por ser uma solução robusta, amplamente utilizada, e de fácil configuração. Ele distribui o tráfego de entrada entre os servidores (app1, app2, app3), garantindo:

1. Desempenho otimizado: O Nginx é altamente eficiente na distribuição de requisições;
2. Alta disponibilidade: Caso um dos servidores do backend falhe, o Nginx pode redirecionar as requisições para outros servidores disponíveis;
3. Escalabilidade: A configuração do Nginx permite facilmente adicionar ou remover servidores de backend.

#### 3. Banco de Dados na AWS RDS (MySQL)
Utilizar o RDS permite escalar o banco de dados de forma automática, além de contar com a robustez e segurança fornecidas pela AWS. A escolha do MySQL como sistema de gerenciamento de banco de dados é devido à sua simplicidade e compatibilidade com a aplicação.

</Details>

<Details> 
  <Summary>
    🔁 Fluxo das Requisições
  </Summary>

</br>

* O usuário acessa o sistema via navegador (porta 80);
* O Nginx recebe a requisição e a redireciona para um servidor de backend;
* O backend processa e consulta o banco de dados, se necessário;
* O Nginx retorna a resposta ao usuário.

</Details> 

---

### ⚙️ Passo a Passo da Configuração - Projeto aws

  * Acesse para ver o passo a passo do [Projeto](./instruções/readme-docker.md)
  * Acesse para ver o passo a passo do [Banco de Dados](./instruções/banco-readme.md) no RDS.

---

### Equipe 
|Nome | GitHub|
| -------- | -------- |
|**Julia Gonzalez**| [![](https://bit.ly/3f9Xo0P)](https://github.com/juliagonzalezmoreira)|
|**Maria Luiza Guedes**| [![](https://bit.ly/3f9Xo0P)](https://github.com/mluizaguedes)|
|**Sofia Lessa**|[![](https://bit.ly/3f9Xo0P)](https://github.com/sofialessaa)|
