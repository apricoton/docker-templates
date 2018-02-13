FROM alpine:edge
RUN apk update && \
    apk upgrade && \
    apk add --no-cache apache2 shadow \
        php7 php7-common php7-xml php7-xmlrpc php7-zip php7-session php7-soap php7-sockets php7-mysqli php7-mysqlnd \
        php7-opcache php7-pdo php7-pdo_mysql php7-fileinfo php7-gd php7-iconv php7-intl php7-json php7-mbstring \
        php7-dom php7-curl php7-apache2 php7-posix php7-tokenizer php7-ctype php7-simplexml \
        perl-dbd-mysql perl-ipc-run perl-crypt-openssl-dsa perl-xml-sax perl-archive-zip perl-gd perl-mozilla-ca \
        perl-digest-sha1 perl-html-parser perl-crypt-ssleay perl-xml-sax-base perl-xml-libxml perl-yaml-syck \
        perl-io-socket-ssl perl-authen-sasl perl-cache-cache perl-xml-parser perl-net-ssleay && \
    rm /var/cache/apk/* && \
    mkdir -p /run/apache2/ && \
    mkdir -p /var/www/app/
RUN usermod -u 1000 apache && \
    groupmod -g 1000 apache
COPY ./entrypoint.sh /

EXPOSE 80
CMD ["/entrypoint.sh"]

