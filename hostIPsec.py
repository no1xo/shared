from scapy.all import IP, TCP, Raw, send
from scapy.layers.ipsec import SecurityAssociation, ESP
import threading

# AES ve HMAC-SHA1 kullanarak IPSec için Güvenlik Birliği (Security Association) oluştur
sa = SecurityAssociation(ESP, spi=0x222,
                         crypt_algo='AES-CBC', crypt_key=b'myencryptionkey',
                         auth_algo='HMAC-SHA1', auth_key=b'myauthenticationkey')

# Gelen şifrelenmiş mesajları çözmek için bir fonksiyon
def decrypt_messages(packet):
    if packet.haslayer(ESP):
        # Paketi deşifre et
        decrypted_packet = sa.decrypt(packet)
        # Deşifre edilen paketi işle
        print("Mesaj alındı:", decrypted_packet[Raw].load)

# Kullanıcıdan mesaj alıp göndermek için bir fonksiyon
def get_and_send_message(dst_ip, dst_port):
    while True:
        message = input("Gönderilecek mesajı yazın: ")
        # Ham IP paketi oluştur
        packet = IP(src='1.1.1.1', dst=dst_ip)/TCP(sport=45012, dport=dst_port)/Raw(load=message)
        # Paketi şifrele
        encrypted_packet = sa.encrypt(packet)
        # Şifrelenmiş paketi gönder
        send(encrypted_packet)

# Gelen paketleri dinlemek için bir thread başlat
threading.Thread(target=lambda: sniff(filter="ip", prn=decrypt_messages)).start()

# Kullanıcıdan mesaj alıp göndermek için bir thread başlat
threading.Thread(target=lambda: get_and_send_message('2.2.2.2', 80)).start()
