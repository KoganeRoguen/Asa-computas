FROM ubuntu:latest

RUN apt update --fix-missing -y
RUN apt upgrade -y
RUN apt install postfix dovecot-imapd dovecot-pop3d -y
RUN apt install -q -y syslog-ng

# Copiar o arquivo de configuração
COPY main.cf /etc/postfix 

# Copiar o arquivo de autenticação do Dovecot
COPY ./dovecot/10-auth.conf /etc/dovecot/conf.d

# Add User
RUN useradd -m roguen
RUN useradd -m hellinsun
RUN useradd -m alisson
# Set user passord
RUN echo "roguen:2711" | chpasswd
RUN echo "hellinsun:2711" | chpasswd
RUN echo "alisson:2711" | chpasswd

#-----------------------------------------------
#CMD ["postfix", "start-fg"]

CMD ["sh", "-c", "service syslog-ng start ; service postfix start ; service dovecot start; tail -F /var/log/mail.log"]