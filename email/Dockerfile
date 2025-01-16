FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install postfix -y

# Copiar o arquivo de configuração
COPY main.cf /etc/postfix 

# Add User
RUN useradd -m roguen
RUN useradd -m hellinsun
RUN useradd -m alisson

# Set user passord
RUN echo "roguen:2711" | chpasswd
RUN echo "hellinsun:2711" | chpasswd
RUN echo "alisson:2711" | chpasswd

#-----------------------------------------------
CMD ["postfix", "start-fg"]

#CMD ["sh", "-c", "/sbin/postfix start", "tail -f /var/log/maillog"]