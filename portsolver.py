#! /usr/bin/env python3

import sys
import subprocess

def connect(server, port):
    print('[+] Connecting...')
    command = 'ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no -p {} {}'.format(port, server)
    ssh_stdout = subprocess.check_output(command, shell=True)
    results = ssh_stdout.decode("utf-8").strip('\n').strip('\r')
    print(results)
    return results

def main():
    server = str(sys.argv[1])
    port = 9000
    high_low = connect(server, port)
    print(high_low)
    while high_low == 'Higher' or high_low == 'Lower':
        if high_low == 'Higher':
            port -= 1
            high_low = connect(server, port)
        elif high_low == 'Lower':
            port += 1
            high_low = connect(server, port)
    print(high_low)
    print('The winning port was: {}'.format(port))

if __name__ == '__main__':
    main()
