

# spyse-subdomain-finder
We all know about the famous spyse this python3 scripts scrounges subdomainswithout the api. There is an option of getting the api, in fact that's what I recommend using the api they provide. Because this methods below may not bring out all subdomains as the api can and perhaps the portability also.

## Installing dependencies
You must have pip installed on your system
```sh
$ git clone https://www.nmmapper.com/sys/tools/subdomainfinder/
$ python3 -m venv myenv

# after activing your virtualenv
pip3 install -r requirements.txt
```

## Basic usage
```sh
$ python3 spyse.py  -d nmmapper.com
[
    "wss.nmmapper.com",
    "webook.nmmapper.com",
    "mail.nmmapper.com",
    "nwebook.nmmapper.com",
    "nmail.nmmapper.com"
]
```

This tool is still in development. If you want a mature  either a script or [subdomain finders hosted online](https://www.nmmapper.com/sys/tools/subdomainfinder/) here are some details.


## Cross-Selling
* [Ethical-tools](https://ethicaltools.gitbook.io/subdomainfinder/)
* [python3-nmap](https://nmap.readthedocs.io/en/latest/)
* [Dnsdumpster](https://dnsdumpster.readthedocs.io/)
* [Aquarium Desk](https://www.aquariumdesk.com/)

