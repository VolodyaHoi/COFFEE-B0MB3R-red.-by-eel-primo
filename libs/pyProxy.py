import requests

class proxyscrape:
    def __init__(self, region = "US", proxy_type = "http"):
        self.region = region
        
        self.type = proxy_type

        print("[!] Using Proxyscrape proxy provider")

    def get_proxy(self, limit=16):
        proxies = requests.get(f"https://api.proxyscrape.com/?request=displayproxies&proxytype={self.type}&country={self.region}", timeout=10).text.split()
        
        if limit > len(proxies):
            print("[!] Limit is greater than the number of proxies!")
            limit = len(proxies)
            
        print("[?] Got", len(proxies),"| checking only", limit)
        
        for proxy in proxies:
            
            if not proxies.index(proxy)+1 > limit:

                print("/------------------***-----------------/")
                print("[!] Progress:", proxies.index(proxy)+1, "out of", limit)
                print("[?] Checking proxy:", proxy)                
                
                try:
                    
                    if requests.get("https://github.com/cd-con", proxies={'http': "http://{}".format(proxy), 'https':"http://{}".format(proxy)}, verify=False, timeout=5).status_code == 200:
                        
                        print("[+] Avaliable")
                        
                        return proxy
                    
                except:
                    
                    print("[-] Timed out/unavaliable")
                    
            else: break
            
        return "localhost:8080"
