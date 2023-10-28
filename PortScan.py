import socket
from optparse import OptionParser
import threading
import sys

class PORT_DIR(threading.Thread):
    def __init__(self, ip, ports, count):
        threading.Thread.__init__(self)
        self._ip = ip
        self._ports = ports
        self._count = count

    def run(self):
        for port in self._ports:
            Port_Scan(self._ip, port, self._count)

def Port_Scan(ip, port, count):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        res = s.connect_ex((ip, port))
        if not res:
            print('[*] IP : {}:{} 已开放'.format(ip, port))
    except:
        pass

def main():
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="你要扫描的IP地址")
    parser.add_option("-f", "--file", dest="file", help="包含端口列表的字典文件")
    parser.add_option("-t", "--thread", dest="count", type="int", default=10, help="扫描威胁系数")
    parser.add_option("-p", "--ports", dest="ports", help="扫描特定端口，以逗号分隔")
    (options, args) = parser.parse_args()

    if options.url:
        ip = options.url

        if options.ports:
            ports = [int(port) for port in options.ports.split(',')]
        else:
            ports = []

        if options.file:
            with open(options.file, 'r') as file:
                lines = file.readlines()
                ports += [int(line.strip()) for line in lines]

        thread_count = min(options.count, len(ports))
        threads = []

        for i in range(thread_count):  #分配线程
            chunk_size = len(ports) // thread_count  # //整除 表示每个线程要处理的端口数
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < thread_count - 1 else len(ports)   #start 和 end 表示当前线程需要处理的端口范围
            chunk = ports[start:end]

            thread = PORT_DIR(ip, chunk, options.count)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
