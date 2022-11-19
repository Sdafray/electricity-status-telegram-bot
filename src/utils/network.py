import os


def is_network_active(ip: str) -> bool:
    response = os.system('ping -c 1 ' + ip + ' >/dev/null 2>&1')
    return response == 0


if __name__ == '__main__':
    print(is_network_active('ip'))
