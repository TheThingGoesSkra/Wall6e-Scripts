#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

import os
import time
import requests 
from itertools import cycle
import traceback
from lxml.html import fromstring

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:20]:
        if i.xpath('.//td[7][contains(text(),"no")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def test_connection():
    try:
        r = requests.get("http://10.10.10.138")
    except:
        test_connection() 

def get_nbLignes_fichier():
    file = open("output_tampon.txt","r")
    numberOfLine = 0
    for line in file:
        numberOfLine += 1
    return numberOfLine

def afficher_fichier():
    with open("output_tampon.txt","r") as fichier:
        texte = fichier.read()
        print(texte)

proxies = get_proxies()
proxy_pool = cycle(proxies)
print(proxies)

url = 'http://10.10.10.138'

proxy = next(proxy_pool)
try:
    response = requests.get(url,proxies={"http": proxy, "https": proxy})
    print(response.json())
except:
    #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
    #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
    print("Skipping. Connnection error")

os.system("cat directory.txt > directory_temp.txt")
print("c'est parti")
tampon = 0
while tampon<299702 :
    os.system('wfuzz -c -z file,directory_temp.txt http://10.10.10.138/FUZZ > output_tampon.txt')
    b = get_nbLignes_fichier()
    b = b - 19
    if b==0:
        break
    tampon = tampon + b
    afficher_fichier() 
    print("Nombre de lignes avant sed : ")
    os.system("wc -l directory_temp.txt")
    os.system("cat directory.txt | sed '1,"+str(tampon)+"d' > directory_temp.txt")
    print("Nombre de lignes après sed :")
    os.system("wc -l directory_temp.txt")
    test_connection()  
    print("c'est reparti")

