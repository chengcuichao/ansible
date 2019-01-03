

HostList = ['192.168.128.221','192.168.128.222','192.168.128.223']

def CreateHostVars(HostList):
    for host in HostList:
        with open('hosts_vars/%s'%host,'w') as f:
            f.write('NodeId: %s'%host.split('.')[-1])

if __name__ ==  '__main__':
    CreateHostVars(HostList)