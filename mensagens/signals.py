from mensagens.models import Uso, Erro
from django.db.models.signals import post_save
import win32com.client
import pythoncom


#___




def recebe_uso(sender, instance, created, **kwargs):
    #PRECISA ESTAR LOGADO NO OUTLOOK
    outlook = win32com.client.Dispatch('outlook.application', pythoncom.CoInitialize())
    mail = outlook.CreateItem(0)

    #EMAIL QUE RECEBE:
    mail.To = 'rafael.cabral@edicoescnbb.com.br'

    mail.Subject = 'Solicitação de Uso'
    mail.HTMLBody = '<h3>This is HTML Body</h3>'
    mail.Body = "Solicitação de Uso recebida"

    mail.Send()

def recebe_erro(sender, instance, created, **kwargs):
    #PRECISA ESTAR LOGADO NO OUTLOOK
    outlook = win32com.client.Dispatch('outlook.application', pythoncom.CoInitialize())
    mail = outlook.CreateItem(0)
    
    #EMAIL QUE RECEBE:
    mail.To = 'rafael.cabral@edicoescnbb.com.br'

    mail.Subject = 'Mensagem informa problemas'
    mail.HTMLBody = '<h3>This is HTML Body</h3>'
    mail.Body = "Mensagem de informação recebida"

    mail.Send()

post_save.connect(recebe_uso, sender=Uso)
post_save.connect(recebe_erro, sender =Erro)