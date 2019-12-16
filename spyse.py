import requests
import useragents
import re
import spyseparser 
import argparse
import simplejson as json 
import socket 

class SpyseSubdomainSearch(object):

    def __init__(self, domain):
        self.domain = self.cleanDomain(domain)
        
        self.referer = "https://spyse.com/search/domain/{0}".format(self.domain)
        self.host = "https://spyse.com/domain/json-subdomains?domain={0}&page=1&per_page=20&q={1}".format(self.domain, self.domain)
        self.host_header = "spyse.com"
        
        self.ua = useragents.UserAgents()
        self.headers = {"User-Agent":self.ua.get_user_agent(),
                        "Host":self.host_header, 
                        "Accept-Language": "en-US,en;q=0.5",
                        "Accept-Encoding":"gzip, deflate, br",
                        "Connection": "keep-alive",
                        "X-Requested-With":"XMLHttpRequest",
                        "Accept":"*/*",
                        "Referer":self.referer
                        }
        
        self.regx = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
        self.compiled = re.compile(self.regx)
        self.results = None
        self.subdomains = []
        # re.findall(r"https?://(?!www\.)(.*\.nmmapper\.com).*", t)
        # re.findall(r"(?!www\.)(.*\.nmmapper\.com).*", tx)
        
    def do_search(self):
        try:
            res = requests.get(self.host, headers=self.headers)
            self.results = res.content.decode('UTF-8')
        except Exception as e:
            print(e)
            
    def get_hostnames(self):
        rawres = spyseparser.SpyseParser(self.results, self)
        rawres.run_parser()
        
        subdomain_parsed = rawres.hostnames
        
        for sub in subdomain_parsed:
            self.subdomains.append({
                "subdomain":sub,
                "ip":self.resolve_ip(sub)
            })
        return self.subdomains 
        
    def process(self):
        print('Beginning subdomain parsing from {0}'.format(self.host_header))
        self.do_search()
        return self.get_hostnames()
    
    def cleanDomain(self, domain):
        """
        Remove https:// www
        """
        return domain.replace("https://", "", len(domain)).replace("http://", "", len(domain)).replace("www", "", len(domain))
    
    def resolve_ip(self, host):
        """
        @ given the host return the IP
        """
        try:
            return socket.gethostbyname(host)
        except socket.gaierror:
            return "404"
            
    def get_people(self):
        return []
    
    def get_ipaddresses(self):
        return []

if __name__=="__main__":
    parser = argparse.ArgumentParser(prog="Search for subdomains from spyse.com")
    parser.add_argument('-d', '--d', help='Help', required=True)
    args = parser.parse_args()
    
    spyse = SpyseSubdomainSearch(args.d)
    subdomains = spyse.process()
    print(json.dumps(subdomains, indent=4, sort_keys=True))
