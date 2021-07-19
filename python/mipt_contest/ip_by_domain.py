"""
Выведите IP-адрес, соответствующий доменному имени. Рекомендуется пользоваться gethostbyname();
"""
import socket


def find_ip(domain: str) -> str:
    return socket.gethostbyname(domain)


print(find_ip(input()))
