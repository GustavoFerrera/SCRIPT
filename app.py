#!/usr/bin/env python
# coding: utf-8

# ### Consumir dados de uma API

# In[ ]:


import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# In[2]:


import requests

link = "https://APIDesligados.gustavoferrei78.repl.co"

requisicao = requests.get(link)


# In[3]:


print(requisicao.json())


# ### DISPARAR TABELA DAS PESSOAS DESLIGADAS

# In[4]:


#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#navegador = webdriver.Chrome()

#entrar no google
#navegador.get("https://apiweb.gustavoferrei79.repl.co/nome/numero_registro")

#navegador.quit()


# In[5]:


from IPython.display import display
import pandas as pd
tabela = pd.read_json("https://APIDesligados.gustavoferrei78.repl.co")
display(tabela)


# In[6]:


tabela.to_excel("Demissoes_tratadas.xlsx", index=False)
from openpyxl import load_workbook
wb = load_workbook('Demissoes_tratadas.xlsx')
ws = wb['Sheet1']
ws.column_dimensions['A'].width = 10
ws.column_dimensions['B'].width = 20
wb.save('Demissoes_tratadas.xlsx')


# In[7]:


import smtplib

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


fromaddr = "testandodisparospy@gmail.com" 
toaddr = "gustavo.ferrera.nasc@gmail.com"

host = "smtp.gmail.com"
port = "587"
login = "testandodisparospy@gmail.com"
senha = "dhfkcqdmtrvvgkfn"

server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.login(login,senha)

corpo = "Colaboradores desligados do dia"
email_msg = MIMEMultipart()
email_msg['From'] = fromaddr
email_msg['To'] = toaddr
email_msg['Subject'] = "Bom dia, está em anexo os colaboradores desligados do dia"
email_msg.attach(MIMEText(corpo,'html'))

cam_arquivo = r"C:\\Users\\106127\\Desktop\\Demissoes_tratadas.xlsx"
attchment = open(cam_arquivo, 'rb')

att = MIMEBase('application', 'octet-stream') 
att.set_payload(attchment.read()) 
encoders.encode_base64(att)

att.add_header('Content-Disposition', f'attachment; filename=Demissoes_tratadas.xlsx')
attchment.close()
email_msg.attach(att)

server.sendmail(fromaddr, toaddr, email_msg.as_string())

server.quit()


# In[8]:


from twilio.rest import Client

account_sid = 'AC4d2b911af8a1aee680601ee9c76099ad'
token = '6446acf04a57eac6e315ba46c1af779b'

client = Client(account_sid, token)

remetente = '+13205924793'
destino = '+5519997068478'

message = client.messages.create(
    to = destino, 
    from_=remetente,
    body="Foi publicado as contas de colaboradores desligados do dia!")

print(message.sid)

