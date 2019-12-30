import sys
i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
sys.stdin, sys.stdout, sys.stderr = i, o, e

def main():
    domain = ""
    if len(sys.argv) == 2:
        domain = sys.argv[1]
    else:
        domain = input("Enter the domain you would like to search for:\n")
    packet = IP(dst='8.8.8.8')/UDP(sport=24603, dport=53)/DNS(qdcount=1)/DNSQR(qname=domain)
    send(packet)
    response = sr1(packet)

    print(response[DNSRR].rdata)

if __name__ == '__main__':
    main()