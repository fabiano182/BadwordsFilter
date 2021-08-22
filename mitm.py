import socket
import codecs
from scapy.all import *
from netfilterqueue import NetfilterQueue
import json

post = "POST"

def print_pacote(pkt):
    #aux = "text="
    pacote = IP(pkt.get_payload())
    dados = pacote[IP].payload
    index = pacote.find("text=")
    print("\n{} ----HTTP---->{}\n".format(pacote[IP].src, pacote[IP].dst))
    if(index != -1):
        print("Conteudo: {}".format(dados[index:]))
    


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
    if((packet[IP].src == "192.168.100.5") and (packet[IP].dst == "192.168.100.10") and packet.haslayer(TCP)):
        dados = str(et)
        if(dados.find(post) != -1):
            et = TCP(find_badword(dados))
            packet[IP].payload = et
            del packet[TCP].chksum
            del packet[IP].ihl
            del packet[IP].len
            del packet[IP].chksum
            packet.show2(dump=True)
            pkt.set_payload(bytes(packet))
            print("#######pacote alterado############")

    pkt.accept()


def forwarder(pkt):
    print_pacote(pkt)
    pkt.accept()


nfqueue = NetfilterQueue()
#nfqueue.bind(0,packet_callback)
nfqueue.bind(0, forwarder)
try:
    print('nfqueue running!')
    nfqueue.run()
except KeyboardInterrupt:
    pass
