## Passo a Passo da VPN

### Passo 1: Conectando no CMD
* Copie o seu Endereço IPv4 público e no terminal escreva:
``` bash
cd Downloads
```
``` bash
ssh -i <nome-da-chave>.pem ubuntu@<ip> #Não esqueça de tirar os <> e só substituir.
```

---
### Passo 2: Configurar a VPN!
* Instale a vpn na sua instância
``` bash
sudo apt update 
sudo apt install openvpn easy-rsa -y
```
``` bash
cd /etc/openvpn/server
sudo touch servidor.conf 
sudo nano servidor.conf
```

* Escreva as seguintes configurações para servidor.conf:
``` bash
dev tun
ifconfig 10.0.0.1 10.0.0.2
secret /etc/openvpn/server/<nome-chave>
port 5000
proto udp
comp-lzo
verb 4
keepalive 10 120
persist-key
persist-tun
float
cipher AES256
```

* Gere a chave e libere a porta 5000 - tipo UDP Personalizado no grupo de segurança:
``` bash
sudo openvpn --genkey secret <nome-chave>
```
``` bash
sudo nano /etc/openvpn/client/client.ovpn

#Escreva isso:
dev tun
proto udp
remote <ip-da-instancia> 5000
ifconfig 10.0.0.2 10.0.0.1
secret <nome-chave>
cipher AES256
comp-lzo
verb 4
keepalive 10 120
persist-key
persist-tun
float

route 10.0.0.1 255.255.255.255
```

* Vamos iniciar e atualizar sua vpn:
``` bash
sudo systemctl start openvpn-server@servidor
sudo systemctl daemon-reload
sudo systemctl restart openvpn-server@servidor #só use se for reconfigurar algo
```

---

### Passo 3: Configurando a VPN no NGINX
* No terminal escreva:
``` bash
cd 
cd <nome-do-repositorio>
cd nginx/
sudo nano default.conf
```

* Edite seu arquivo default.conf:
``` bash
upstream backend {
        server app1:5000 weight=3;
        server app2:5000 weight=1;
        server app3:5000 weight=1;
}

server {
         listen 10.0.0.1:80; #Altere aqui, apenas adicione 10.0.0.1

         location / {
                proxy_pass http://backend;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
        }
}
```
* Rebuilde o docker
``` bash
sudo docker-compose up --build -d
```

---

### Passo 4:  
``` bash
cd 
cd /etc/openvpn/client
sudo cp client.ovpn /home/ubuntu #copio para o ubuntu para ser acessivel pro scp
```
``` bash
cd /etc/openvpn/server
sudo chmod 404 <nome-chave>
sudo cp <nome-chave> /home/ubuntu
exit
```

---

### Passo 5
* No terminal, ainda em Downloads, escreva:
``` bash
scp -i <chave-aws>.pem ubuntu@<ip-da-instancia>:/home/ubuntu/<nome-chave> .
scp -i <chave-aws>.pem ubuntu@<ip-da-instancia>:/home/ubuntu/client.ovpn .
```

---

### Passo 6: Instalar OpenVPN e configurar
* Acesse o site abaixo para baixar o OpenVPN e instale o “Windows 64-bit MSI installer”: [Site OpenVPN](https://openvpn.net/community-downloads/)
* Você vai receber um aviso como este:

  ![image](https://github.com/user-attachments/assets/b263ca70-caa8-4bb4-b187-d62bc6570c49)

* Abra o Explorador de Arquivose manualmente e vá até a pasta, no meu caso: C:\Users\matos\OpenVpn\config
* Abra outro Explorador de Arquivos, vou em Downloads e copio os arquivos (<nome-chave> e client) para C:\Users\matos\OpenVpn\config

  ![image](https://github.com/user-attachments/assets/c5801e05-0cc8-4ecd-9b0a-c1e20b89e2ac)

* No canto inferior direito da sua máquina, abra igual mostra a foto e clique em SAIR

  ![image](https://github.com/user-attachments/assets/840ecb6c-6cdc-4f47-b702-da01fb564eb3)

* Execute como administrador o OpenVPN

  ![image](https://github.com/user-attachments/assets/843207c1-367e-43fb-a9f3-f703f77f1cfd)

⚠️ Lembre-se: sempre que for se conectar à sua instância, não se esqueça de substituir o <ip-da-instância> pelo IP correto no arquivo client.ovpn
