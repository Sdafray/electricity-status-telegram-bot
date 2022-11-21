import os


def is_network_active(ip: str) -> bool:
    responses = list()
    for n in range(0, 2):
        responses.append(os.system(f'ping -c 1 {ip} >/dev/null 2>&1'))
    return sum(responses) == 0


# test
if __name__ == '__main__':
    print(is_network_active('ip'))
