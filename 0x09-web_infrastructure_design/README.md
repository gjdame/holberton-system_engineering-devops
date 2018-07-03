0x09 Web Infastructure

Links in files to diagram of basic web infastructures

0-simple_web_stack

1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

1-distributed_web_infrastructure

In addition to the structure from #0

2 servers
1 web server (Nginx)
1 application server
1 load-balancer (HAproxy)
1 application files (your code base)
1 database (MySQL)

2-secured_and_monitored_web_infrastructure

In addition to the structure from #1

3 firewalls
1 SSL certificate to serve www.foobar.com over HTTPS
3 monitoring clients (data collector for Sumologic or other monitoring services)


3-scale_up

In addition to the structure from #2

1 server
1 load-balancer (HAproxy) configured as cluster with the other one
Split components (web server, application server, database) with their own server