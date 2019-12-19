#  utils.py
#  
#  Copyright 2019 Wangolo Joel <wangolo@ldap.testlumiotic.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import requests
import useragents

#from wafw00f.main import WafW00F

def add_protocol(h):
    """
    Add https in domain
    """
    if(h.startswith("https") or h.startswith("http")):
        return h
    else:
        return "http://" + h
        
def get_server_type(host):
    """
    :param host: the server we want to get it's server
    @return str
    """
    try:
        ua = useragents.UserAgents()
        headers = {
            'User-Agent': ua,
            'From': 'info@nmmapper.com' 
        }
        res  = requests.get(add_protocol(host), headers=headers)
        if(res.headers):
            return res.headers.get("Server")
        else:
            return ""
            
    except Exception as e:
        return ""
        
def detect_waf(host): # NOT IMPLEMENTED YET
    """
    :param host: Detect if the host is behind web application firewall
    @return str
    """
    try:
        detector = WafW00F(host)
        waf = detector.identwaf()
        if(waf):
           return waf[0]
        else:
            return ""
    except Exception as e:
        print(e)
        return ""
        
