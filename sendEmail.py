import smtplib
from email.mime.text import MIMEText

def sendEmail(username,password,destino,assunto,conteudo):
  # conexão com os servidores do google
  smtp_ssl_host = 'smtp.gmail.com'
  smtp_ssl_port = 465

  message = MIMEText(conteudo)#conteudo
  message['subject'] = assunto
  message['from'] = username#remetente
  message['to'] = ', '.join(destino)#destinatario

  # conectaremos de forma segura usando SSL
  server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
  # para interagir com um servidor externo precisaremos
  # fazer login nele
  server.login(username, password)
  server.sendmail(username, destino, message.as_string())
  server.quit()
