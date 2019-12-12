# spyse-subdomain-finder
We all know about the famous spyse.com this python3 scripts scrounges [subdomains](https://www.nmmapper.com/sys/tools/subdomainfinder/) without the api.
There is an option of getting the api, in fact that's what I recommend using the api they provide. Because this methods below may not bring out all [subdomains](https://www.nmmapper.com/sys/tools/subdomainfinder/) as the api can and perhaps the portability also.

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

This tool is still in development. If you want a mature [subdomain finder](https://www.nmmapper.com/sys/tools/subdomainfinder/) either a script or [subdomain finders hosted online](https://www.nmmapper.com/sys/tools/subdomainfinder/) here are some details.
## Other none api subdomain finder
* [Censys none api](https://github.com/wangoloj/censys-subdomain-finder-non-api.git)
* [Dnsdumpster script](https://github.com/wangoloj/dnsdumpster.git)
* [8 Subdomain finder tools online](https://www.nmmapper.com/sys/tools/subdomainfinder/)
