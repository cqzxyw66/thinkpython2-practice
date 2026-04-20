import os
import dns.resolver
import httplib2
import sys

appdomain = []
port_list = []

def script_check():
    global appdomain, port_list
    if len(sys.argv) < 3:
        domain_input = input('请输入你要监控的域名：').split(',')
        port_list_input = input('请输入你要监控的端口：').split(',')
        appdomain += domain_input
        port_list += port_list_input
    else:
        appdomain += sys.argv[1].split(',')
        port_list += sys.argv[2].split(',')
    assert isinstance(port_list, list) and isinstance(appdomain, list)

def get_iplist(domain=''):
    iplist = []
    try:
        A = dns.resolver.resolve(domain, 'A')
    except:
        return False
    for i in A.response.answer:
        if i.rdtype._name_ == 'A':
            for j in i.items:
                iplist.append(j.address)
    return iplist
            
def check(domain):
    domain_fqdn, domain_port = domain.split(':')[0], domain.split(':')[1]
    h = httplib2.Http(disable_ssl_certificate_validation=True)

    iplist = get_iplist(domain_fqdn) if get_iplist(domain_fqdn) else None
    header = {'Host':domain_fqdn, 'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x66) AppleWebKit/537.36'}

    print(domain)
    for ip in iplist:
        url = 'http://' + ip + ':' + domain_port if domain_port == 80 else 'https://' + ip + ':' + domain_port
        resp, content = h.request(url, method='GET', headers=header)
        result = resp.status

        if result == 200:
            print(ip, '[OK]')
        else:
            print(ip, '[Error]')

if __name__ == '__main__':
    script_check()
    for domain in appdomain:
        try:
            if len(get_iplist(domain)) > 0:
                for j in port_list:
                    domain_full = domain + ':' + j
                    check(domain_full)
        except Exception,TypeError:
            print('dns resolver error')