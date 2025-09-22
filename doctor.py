import ollama
import hashlib, os
from pypdf import PdfReader

database = '.\\db'

def login(): return hashlib.sha256(input('Please enter username : ').encode('utf8')).hexdigest()






cookie = login()
if cookie not in os.listdir(database):
    os.mkdir(database+'.\\'+cookie)
    os.mkdir(database+'\\'+cookie+'\\'+'rec')
    os.mkdir(database+'\\'+cookie+'\\'+'chat')

os.chdir(database+'\\'+cookie)


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def genRateResponce():
    recFile = []
    chatFile = []
    for rec in os.listdir('.\\rec'):
        recFile.append(extract_text_from_pdf('.\\rec'+'\\'+rec))
    
    for chat in os.listdir('.\\chat'):
        with open('.\\chat\\'+chat) as a:
            a.read()
        chatFile.append()
    
    print()

while True:
    a = input('a. Upload a health report\nb. Explain your symptoms\nChose : ').lower()
    if a == 'a':
        pass
    elif a == 'b':
        pass

response = ollama.generate(model='medllama2', prompt='Why is the sky blue?')
print(response['response'])