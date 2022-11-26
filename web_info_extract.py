import re
import requests
from bs4 import BeautifulSoup

class ContactInfo:
    def __init__(self, url):      
        self.url = url

    def fetch_contact(self):
        links = []
        soup = BeautifulSoup(requests.get(self.url).content, 'html.parser')
        for anchor in soup.findAll("a"):
            href = anchor.attrs.get("href")
            links.append(href)

        return links

    def link_types(self, links):
        general_domains = ["facebook", "linkedin", "twitter", "instagram", "pinterest"]
        social_links = []
        emails = []
        contacts = [] 
        for url in links:
            for gen_link in general_domains:
                if gen_link in url:
                    social_links.append(url)

            if 'mailto:' in url:
                url = re.sub('mailto:','',url)                
                emails.append(url)
            
            if 'tel:' in url:
                url = re.sub('tel:','',url)
                contacts.append(url)
        
        return social_links, emails, contacts        

if __name__ == '__main__':
    url = input("Url : ")
    links = ContactInfo(url).fetch_contact()
    social_links, email_addr, contacts = ContactInfo(url).link_types(links)
    print(f'social links : {social_links}\nemails : {email_addr}\ncontacts : {contacts}')