## Trabalho Prático: Infraestrutura de Rede Integrada para a Empresa XPTO

### 📍 Objetivo: 
Projetar e implementar uma infraestrutura de TI robusta para a empresa XPTO integrando tecnologias modernas de redes e segurança. O projeto deve incluir um ambiente de acesso remoto seguro, gerenciamento de tráfego e serviços virtualizados, garantindo confiabilidade e eficiência para a organização. 

---

### 📝 Requisitos:
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

---

### Passo a passo:
  * #### Passo 1 -> Acesse sua AWS e crie uma instância! -> Vá em "Executar Instâncias".
![image](https://github.com/user-attachments/assets/a12b1c91-963c-4b2c-b569-c01d94d5f13b)
