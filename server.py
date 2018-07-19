import re, json
from local_settings import local_server

list_servers = [
    local_server,
    {'name':'HOMOLOGA','host':'192.168.25.93','port_number':22,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.OPTIMUS-CLOUD-01'},
    #{'name':'OPTIMUS-INTERVALOR-01','host':'10.100.31.72','port_number':22,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full.SRVVAAPP02'},
    {'name':'OPTIMUS-INTERVALOR-02','host':'10.100.31.75','port_number':22,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full.SRVVAAPP04 '},
    {'name':'OPTIMUS-INTERVALOR-03','host':'10.100.31.77','port_number':22,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.SRVAAPP06'},
    {'name':'OPTIMUS-INTERVALOR-04','host':'10.100.31.78','port_number':22,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.SRVVAAPP07'},
    {'name':'OPTIMUS-INTERVALOR-05','host':'10.100.31.79','port_number':22,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.SRVVAAPP08'},
    {'name':'OPTIMUS-INTERVALOR-06','host':'10.100.31.80','port_number':22,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.SRVVAAPP09'},
    {'name':'OPTIMUS-INTERVALOR-07','host':'10.100.31.81','port_number':22,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.SRVVAAPP10'},
    {'name':'OPTIMUS-CLOUD-01','host':'200.201.128.218','port_number':2261,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full.OPTIMUS-CLOUD-01'},
    #{'name':'OPTIMUS-CLOUD-02','host':'200.201.128.218','port_number':2262,'optimus':'home', 'log_file':'full'},
    {'name':'OPTIMUS-CLOUD-04','host':'200.201.128.218','port_number':2264,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.OPTIMUS-CLOUD-04'},
    {'name':'OPTIMUS-CLOUD-06','host':'200.201.128.218','port_number':2266,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full'},
    {'name':'OPTIMUS-CLOUD-07','host':'200.201.128.218','port_number':2267,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.OPTIMUS-CLOUD-07'},
    {'name':'OPTIMUS-CLOUD-08','host':'200.201.128.218','port_number':2268,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.OPTIMUS-CLOUD-08'},
    ##{'name':'OPTIMUS-ULTRA-04','host':'192.168.4.44','port_number':22,'pwd':'Topt!@#H7v&','optimus':'home', 'log_file':'full.OPTIMUS-CLOUD-01'},
    ##{'name':'OPTIMUS-ULTRA-05','host':'192.168.4.45','port_number':22,'pwd':'Topt!@#H7v&','optimus':'home', 'log_file':'full.OPTIMUS-CLOUD-01'},
    ##{'name':'OPTIMUS-ULTRA-06','host':'192.168.4.46','port_number':22,'pwd':'Topt!@#H7v&','optimus':'opt', 'log_file':'full.OPTIMUS-CLOUD-01'},
    ##{'name':'OPTIMUS-ULTRA-07','host':'192.168.4.47','port_number':22,'pwd':'Topt!@#H7v&','optimus':'opt', 'log_file':'full.OPTIMUS-CLOUD-01'},
    ##{'name':'OPTIMUS-ULTRA-08','host':'192.168.4.48','port_number':22,'pwd':'Topt!@#H7v&','optimus':'home', 'log_file':'full.OPTIMUS-CLOUD-01'},
    ##{'name':'OPTIMUS-ULTRA-09','host':'192.168.4.49','port_number':22,'pwd':'Topt!@#H7v&','optimus':'opt', 'log_file':'full.OPTIMUS-CLOUD-01'},
    ##{'name':'OPTIMUS-ULTRA-10','host':'192.168.4.43','port_number':22,'pwd':'Topt!@#H7v&','optimus':'opt', 'log_file':'full.OPTIMUS-CLOUD-01'},
    ##{'name':'OPTIMUS-TELIUM-01','host':'200.170.220.147','port_number':2271,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full.OPTIMUS-TELIUM-01'},

    {'name':'OPTIMUS-TELIUM-02','host':'200.170.220.147','port_number':2272,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full.OPTIMUS-TELIUM-02'},
    {'name':'OPTIMUS-TELIUM-03','host':'200.170.220.147','port_number':2273,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full.OPTIMUS-TELIUM-03'},
    {'name':'OPTIMUS-TELIUM-06','host':'200.170.220.147','port_number':2276,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full.OPTIMUS-TELIUM-06'},
    {'name':'OPTIMUS-TELIUM-07','host':'200.170.220.147','port_number':2277,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.OPTIMUS-TELIUM-07'},
    {'name':'OPTIMUS-TELIUM-08','host':'200.170.220.147','port_number':2278,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.OPTIMUS-TELIUM-08'},
    {'name':'OPTIMUS-TELIUM-10','host':'200.170.220.147','port_number':2280,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.OPTIMUS-TELIUM-10'},
    ## {'name':'OPTIMUS-TRESTTO-03','host':'192.168.25.53','port_number':22150,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full'},
    ##{'name':'OPTIMUS-TRESTTO-04','host':'192.168.25.54','port_number':22,'pwd':'opt!@#H7v','optimus':'home', 'log_file':'full'},
    ##{'name':'OPTIMUS-SERVICES-01','host':'189.112.36.196','port_number':2251,'pwd':'opt!@#H7v','optimus':'opt', 'log_file':'full.OPTIMUS-SERVICES-01'}
]


def server_input():
    name = input("Informe o servidor: ")
    if re.search('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5})',name):
        for server in list_servers:
            if name == server['host'] + ':' + str(server['port_number']):
                host = 'root@' + server['host'] + ':' + str(server['port_number'])
                pwd = {'root@' + server['host'] + ':' + str(server['port_number']) : server['pwd']}

    elif name == 'all':
        host = []
        pwd = {}
        for server in list_servers:
            if 'ULTRA' not in server['name'] and len(server['name'].split("-"))==3:
                host.append('root@' + server['host'] + ':' + str(server['port_number']))
                pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']
    elif name == 'ultra':
        host = []
        pwd = {}
        for server in list_servers:
            if 'ULTRA' in server['name'] and len(server['name'].split("-"))==3:
                host.append('root@' + server['host'] + ':' + str(server['port_number']))
                pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']
    elif name == 'ultra_opt':
        host = []
        pwd = {}
        for server in list_servers:
            if 'ULTRA' in server['name'] and len(server['name'].split("-"))==3:
                if server['optimus']=='opt':
                    host.append('root@' + server['host'] + ':' + str(server['port_number']))
                    pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']
    elif name == 'ultra_home':
        host = []
        pwd = {}
        for server in list_servers:
            if 'ULTRA' in server['name'] and len(server['name'].split("-"))==3:
                if server['optimus']=='home':
                    host.append('root@' + server['host'] + ':' + str(server['port_number']))
                    pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']
    elif name == 'all_opt':
        host = []
        pwd = {}
        for server in list_servers:
            if 'ULTRA' not in server['name'] and len(server['name'].split("-"))==3:
                if server['optimus']=='opt':
                    host.append('root@' + server['host'] + ':' + str(server['port_number']))
                    pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']
    elif name == 'all_home':
        host = []
        pwd = {}
        for server in list_servers:
            if 'ULTRA' not in server['name'] and len(server['name'].split("-"))==3:
                if server['optimus']=='home':
                    host.append('root@' + server['host'] + ':' + str(server['port_number']))
                    pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']


    elif re.search('(\w*)-(\w*)-(\d{2})',name):
        host = []
        pwd = {}
        for server in list_servers:
            if server['name'].lower() == name.lower():
                host.append('root@' + server['host'] + ':' + str(server['port_number']))
                pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']
    elif re.search('(\w*)-(\w*)',name):
        host = []
        pwd = {}
        for server in list_servers:
            if name in server['name']:
                host.append('root@' + server['host'] + ':' + str(server['port_number']))
                pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']
    else:
        host = []
        pwd = {}
        for server in list_servers:
            if server['name'].lower() == name.lower():
                host.append('root@' + server['host'] + ':' + str(server['port_number']))
                pwd['root@' + server['host'] + ':' + str(server['port_number'])] = server['pwd']
    return host, pwd

def list_all_server():
    l = []
    for server in list_servers:
        l.append(server['host'] + ':' + str(server['port_number']))

    print(l)
    return l
