arquive = open('IPs.txt', 'w')
arquive.write('200.135.80.9 \n')
arquive.write('192.168.1.1 \n')
arquive.write('8.35.67.74 \n')
arquive.write('257.32.4.5 \n')
arquive.write('85.345.1.2 \n')
arquive.write('1.2.3.4 \n')
arquive.write('9.8.234.5 \n')
arquive.write('192.168.0.256 \n')
arquive.close()

ip = {}
allip = []

arquive = open('IPs.txt', 'r')
for i in arquive:
    ip = {'ip': i.strip(), 'val': True}
    ips = i.strip().split('.')
    for part in ips:
        if int(part) > 224:
            ip['val'] = False
            break
    allip.append(ip)
for dic in allip:
    if dic['val']:
        print(f'\033[32mO IP: {dic["ip"]} Está Correto\033[m')
    else:
        print(f'\033[31mO IP: {dic["ip"]} Está Errado\033[m')
arquive.close()
