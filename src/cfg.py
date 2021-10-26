import os
import requests

FILE_NAME = os.environ['FILE_NAME']
IADOPT_CFG = os.environ['IADOPT_CFG']
TTL_URL = os.environ['TTL_URL']

vocab = requests.get(TTL_URL).content.decode('UTF-8')
vocab = vocab.replace("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .", IADOPT_CFG)


file = open(f'{FILE_NAME}.ttl', "w")
file.write(vocab)
file.close()