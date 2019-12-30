import sys
i, o, e = sys.stdin, sys.stdout, sys.stderr
from scapy.all import *
sys.stdin, sys.stdout, sys.stderr = i, o, e

SWITCH = 1

def get_reversed(string):
    string = str(string)
    ls = string.split('.')
    ret = ""
    for i in ls[::-1]:
        ret += i + '.'

    return ret[:-1]

def lookup(domain):
    packet = IP(dst='8.8.8.8') / UDP(sport=24603, dport=53) / DNS(qdcount=1) / DNSQR(qname=domain)
    response = sr1(packet)

    print(response[DNSRR].rdata)

def rev_lookup(ip):
    packet = IP(dst='8.8.8.8') / UDP(sport=24603, dport=53) / DNS(qdcount=1) / DNSQR(
        qname=get_reversed(ip) + '.in-addr.arpa', qtype='PTR')
    response = sr1(packet)

    print(response[DNSRR].rdata.decode())


def main():
    domain = ""
    if len(sys.argv) == 2:
        domain = sys.argv[1]
        lookup(domain)
    elif len(sys.argv) == 1:
        domain = input("Enter the domain you would like to search for:\n")
        lookup(domain)
    elif len(sys.argv) == 3 and sys.argv[SWITCH] == '-r':
        ip = str(sys.argv[2])
        rev_lookup(ip)
    else:
        print("Usage: nslookup [domain][-r ip]")
        exit(1)




if __name__ == '__main__':
    main()