
# MeowTuber
Troca badwords (nome de youtubers) por nome de gatinhos

## Instalando o Flask
Execute no terminal:
```
sudo pip3 install Flask
```

## Instalando o Scapy
```
sudo pip3 install scapy
```

## Instalando o NetFilterQueue
```
sudo apt install build-essential libnetfilter-queue-dev 
sudo pip3 install --upgrade -U git+https://github.com/kti/python-netfilterqueue
```
### Instalando o HTTPERF
```
sudo apt install httperf
```

### Criando a interface de rede virtual para o server
```
sudo ifconfig enp0s3:0 192.168.100.10
sudo ifconfig enp0s3:0 netmask 255.255.255.0
```

### Configurar o iptables
```
sudo iptables -I INPUT -d 192.168.100.5/24 -j NFQUEUE
```

### Iniciando o Scapy e NetFilterQueue
```
sudo python3 mitm.py
```

## Rodando a aplicação WEB (Flask)
A aplicação deve ser executada na interface de rede virtual, lembre-se de alterar o host no script
```
python3 main.py
```
