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
        self.seq = kwargs.get('seq')

    def createIpPacket(self):
        ip = scapy.IP(src=self.src, dst=self.dst)
        return ip


    def setMultipleFlags(self, ip):
        #ip = scapy.IP(src=self.src, dst=self.dst)
        tcp = ip/scapy.TCP(sport=self.src_port, dport=self.dst_port,
                           flags=self.flags, seq=123, ack=1) / "scapy packet 123"
        return tcp


    def sendSynPacket(self, ip):
        SYNACK = None
        #ip = scapy.IP(src=self.src, dst=self.dst)
        SYN = scapy.TCP(sport=self.src_port, dport=self.dst_port, flags='S', seq=self.seq)
        try:
            SYNACK = scapy.sr1(ip / SYN)
        except scapy.select_error as e:
            print("Failed to send SYN Packet: %s" % e)
        return SYNACK


    def sendAckPacket(self, ip, SYNACK):
        ACK = scapy.TCP(sport=self.src_port, dport=self.dst_port, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
        try:
            scapy.send(ip / ACK)
        except scapy.select_error as e:
            print("Failed to send ACK Packet: %s" % e)


    def sendPacket(self, packet):
        try:
            scapy.send(packet)
        except scapy.error as e:
            print("packet dropped due to reason: %s" % e)


def main():
    c = PacketCrafting(src="192.168.1.3", dst="192.168.1.1", dst_port=80, seq=2000)
    ip = c.createIpPacket()
    # XMAS attack
    pack = c.setMultipleFlags(ip)
    c.sendPacket(pack)
    # Three way TCP handshake
    synack = c.sendSynPacket(ip)
    c.sendAckPacket(ip, synack)


if __name__=='__main__':
    main()