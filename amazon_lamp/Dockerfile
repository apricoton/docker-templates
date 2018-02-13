FROM amazonlinux:latest
RUN yum -y update && \
    yum -y install \
        httpd24 php70 php70-cli php70-common php70-gd php70-intl php70-json \
        php70-mbstring php70-mcrypt php70-mysqlnd php70-pdo php70-xml \
        php70-xmlrpc php70-zip sendmail
RUN /bin/cp -f /usr/share/zoneinfo/Japan /etc/localtime && \
    echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock
RUN usermod -u 1001 apache && \
    groupmod -g 1001 apache

EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]