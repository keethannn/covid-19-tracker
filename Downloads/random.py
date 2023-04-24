import nmap

def scan_network():
    # Initialize the nmap object
    nm = nmap.PortScanner()
    
    # Scan the network with the given IP range
    nm.scan('192.168.2.1/24', arguments='-sP')

    # Iterate through the hosts found in the scan
    for host in nm.all_hosts():
        print('Host: {}'.format(host))
        print('State: {}'.format(nm[host].state()))
        print('MAC Address: {}'.format(nm[host].mac()))
        print('Protocols: {}\n'.format(nm[host].all_protocols()))

if __name__ == '__main__':
    scan_network()