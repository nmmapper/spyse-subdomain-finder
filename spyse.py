import requests
import useragents
import re
import spyseparser 
import argparse
import simplejson as json 
import socket 
import utils 

class SpyseSubdomainSearch(object):

    def __init__(self, domain):
        self.domain = self.cleanDomain(domain)
        self.limit=20
        self.offset=0
        
        self.referer = "https://spyse.com/"
        self.api_host="https://spyse.com/api/data/domain/subdomain?limit={0}&offset={1}&domain={2}".format(self.limit, self.offset, self.domain)
        self.host_header = "spyse.com"
        
        self.ua = useragents.UserAgents()
        self.headers = {"User-Agent":self.ua.get_user_agent(),
                        "Host":self.host_header, 
                        "Accept-Language": "en-US,en;q=0.5",
                        "Accept-Encoding":"gzip, deflate, br",
                        "Connection": "keep-alive",
                        "Referer":self.referer,
                        "Accept":"application/json, text/plain, */*"
                        }
        
        self.regx = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
        self.compiled = re.compile(self.regx)
        self.results = {}
        self.subdomains = []
        
    def do_search(self):
        try:
            res = requests.get(self.api_host, headers=self.headers)
            if(res.status_code == 200):
                self.results = res.json()
        except Exception as e:
            print(e)
            
    def get_hostnames(self):
        
        if not self.results:
            return self.subdomains 
            
        if not self.results.get("data"):
            return self.subdomains 
            
        if not self.results.get("data").get("items"):
            return self.subdomains
        
        items = self.results.get("data").get("items")

        for sub in items:
            self.subdomains.append({
                "subdomain":sub.get("name"),
                "ip":self.resolve_ip(sub.get("name")),
                "server":utils.get_server_type(sub)
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
