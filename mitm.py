import socket
import codecs
from scapy.all import *
from netfilterqueue import NetfilterQueue
import json

post = "POST"

def print_pacote(pkt):
    packet = IP(pkt.get_payload())
    dados = str(Ether(pkt.get_payload())[Raw].load)
    print(f"\n{packet[IP].src} ----HTTP /POST ----> {packet[IP].dst}\n")
    index = dados.find('text=')
    if(index != -1):
        print(f"Conteudo: {str(dados)[index:]}")

def find_badword(dados):
    with open('badwords.json') as data_file:
        data = json.load(data_file)
        for x in data["badwords"]:
            dados = dados.replace(str(x["badword"]), len(str(x["badword"]))*"*")

    return dados


def packet_callback(pkt):
    packet = IP(pkt.get_payload())
    try:
        et = packet[IP].payload
    except:
        var = 1
    if((packet[IP].src == "192.168.100.4") and (packet[IP].dst == "192.168.100.10") and packet.haslayer(TCP)):
        dados = str(et)
        if(dados.find(post) != -1):
            et = TCP(find_badword(dados))
            packet[Raw].load = et
            #del packet[TCP].chksum
            #del packet[IP].ihl
            #del packet[IP].len
            #del packet[IP].chksum
            print(packet)
            #packet.show2(dump=True)
            #pkt.set_payload(bytes(packet))
            #print("#######pacote alterado############")

    forwarder(pkt)


def forwarder(pkt):
    print_pacote(pkt)
    pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(0,packet_callback)
#nfqueue.bind(0, forwarder)
try:
    print('nfqueue running!')
    nfqueue.run()
except KeyboardInterrupt:
    pass
