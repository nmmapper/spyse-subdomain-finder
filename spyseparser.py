import random
import re

class SpyseParser(object):
    """
    This object will handle the parsing of resuls which wil be in html tables
    """
    def __init__(self, html_results, caller):
        """
        @caller -> the class that has instatiated us
        """
        self.html_results = html_results 
        self.caller = caller 
        self.regx = ""
        self.compiled = ""
        self.domain = ""
        
        if(self.caller):
            self.regx = self.caller.regx
            self.compiled = self.caller.compiled
            self.domain = self.caller.domain 
            
        else:
            self.regx = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
            self.compiled = re.compiled(self.regx)
        
        self.hostnames = []
    
    def run_parser(self):
        """
        Begin querying for domains in the returned table,
        sort duplicates, sort only wanted domains as we shall
        parse even unwated domains
        """
        try:
            domains = self.compiled.findall(self.html_results)
            if(domains):
                # Begin by filtering duplicates and filter only the domains
                # we actually want
                domains = list(dict.fromkeys(domains))
                self.hostnames = [ d for d in domains if self.domain in d ]
                return self.hostnames
                
            self.hostnames = domains # Nothing found
            return self.hostnames 
        except Exception as e:
            raise
    
