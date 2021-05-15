import random
import scapy.all as scapy


class PacketCrafting:
    def __init__(self, **kwargs):
        self.src = kwargs.get('src')
        self.dst = kwargs.get('dst')
        self.dst_port = kwargs.get('dst_port')
        self.src_mac = kwargs.get('src_mac')
        self.flags = kwargs.get('flags')
        self.src_port = random.randint(1024,65535)

    def setMultipleFlags(self):
        ip = scapy.IP(src=self.src, dst=self.dst)
        tcp = ip/scapy.TCP(sport=self.src_port, dport=self.dst_port,
                           flags=self.flags, seq=123, ack=1) / "scapy packet 123"
        return tcp

    def sendPacket(self, packet):
        try:
            scapy.send(packet)
        except scapy.error as e:
            print("packet dropped due to reason: %s" % e)


def main():
    c = PacketCrafting(src="192.168.1.3", dst="192.168.1.1", dst_port=135, flags="PUSAFR")
    pack = c.setMultipleFlags()
    c.sendPacket(pack)


if __name__=='__main__':
    main()