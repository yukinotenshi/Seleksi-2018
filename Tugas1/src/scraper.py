import requests
from bs4 import BeautifulSoup as bs
import json
import os

class Scraper:
    '''A class to scrape shodan.io through the regular search page'''
    def __init__(self, username : str, password : str, proxy=""):
        self.username = username
        self.password = password
        self.session = requests.session()
        if len(proxy):
            proxies = {
                "http" : proxy,
                "https" : proxy
            }
            self.session.proxies.update(proxies)

        self.session.headers.update({
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
        })
        self.data = []

    def login(self):
        '''Login to shodan.io with shodan account specified'''
        r = self.session.get('https://account.shodan.io/login')
        bs1 = bs(r.text, 'html.parser')
        csrf = bs1.find('input', {'name' : 'csrf_token'}).get('value')

        data = {
            "username" : self.username,
            "password" : self.password,
            "grant_type" : "password",
            "continue" : "https://account.shodan.io/",
            "csrf_token" : csrf,
            "login_submit" : "Log in"
        }

        r = self.session.post("https://account.shodan.io/login", data=data)

    def save(self, filename: str):
        '''Save scraped data to json file'''
        with open(filename, 'w') as f:
            json.dump(self.data, f, sort_keys=True, indent=2)

    def scrape_services(self, link: str):
        '''Scrape service detail from a specified host
           Including : host, port, city, country, organization, protocol.
        '''
        print("Scraping host : %s" % (link.split('/')[-1]))
        r = self.session.get(link)
        bs1 = bs(r.text, 'html.parser')
        services = bs1.find_all("li", {"class" : "service service-long"})
        host_detail = bs1.find('table', {'class' : 'table'}).find_all('th')

        data = {
            "host" : link.split('/')[-1],
            "city" : host_detail[0].text,
            "country" : host_detail[1].text,
            "organization" : host_detail[2].text,
            "services" : []
        }

        for service in services:
            data["services"].append({
                "port" : int(service.find("div", {"class" : "port"}).text.strip()),
                "protocol" : service.find("div", {"class" : "protocol"}).text.strip(),
                "name" : service.find("div", {"class": "state"}).text.strip(),
                "detail" : service.find("div", {"class" : "service-main"}).text.strip()
            })

        self.data.append(data)

    def scrape_search_page(self, page : str):
        '''Scrape list of hosts from the i-th search page'''
        bs1 = bs(page, 'html.parser')
        result = bs1.find_all('a', {'class' : 'details'})
        links = ["https://shodan.io" + x.get('href') for x in result]

        for link in links:
            tries = 0
            while tries < 3:
                try:
                    self.scrape_services(link)
                    break
                except:
                    tries += 1

    def scrape_from_keyword(self, keyword:str, limit = 1000, start_from=0):
        '''Get search result from specified search keyword
           start_from = page offset
           limit = how many result you want to scrape
        '''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        limit = limit if limit < 2000 else 2000
        for i in range(int(limit/10)):
            print("Scraping page %d" % (i+1+start_from))
            r = self.session.get("https://www.shodan.io/search?query=%s&page=%d" % (keyword, i+1+start_from))
            try:
                self.scrape_search_page(r.text)
            except:
                print("Skipping page %s" % int(i+1+start_from))

            if i % 5 == 0:
                self.save("%s/../data/autosave-%s.json" % (dir_path, keyword))

    @classmethod
    def load_config(cls):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open('%s/config.txt' % dir_path) as f:
            config = json.load(f)

        if config['use_proxy']:
            instance = Scraper(config['username'], config['password'], config['proxy'])
        else:
            instance = Scraper(config['username'], config['password'])

        try:
            instance.login()
        except Exception as e:
            print(e)
            print("Error during login... please check you connection and credentials")
            exit()

        for keyword, value in config['search_config'].items():
            print("Scraping keyword %s" % (keyword))
            instance.scrape_from_keyword(keyword, value['limit'], value['start_from'])

        instance.save("%s/../data/%s" %(dir_path, config['filename']))

if __name__ == "__main__":
    Scraper.load_config()
