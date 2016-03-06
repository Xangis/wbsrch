server {
        listen 80;
        server_name 216.151.17.10;
        rewrite ^/(.*) https://wbsrch.com/$1;
       }

server {
        listen 80;
        server_name 216.151.17.12;
        rewrite ^/(.*) https://wbsrch.com/$1;
       }

server {
	listen 80;
	server_name www.wbsrch.com;
	rewrite ^/(.*) https://wbsrch.com/$1 permanent;
	}

server {
	listen 80 default;
	server_name *.wbsrch.com wbsrch.com;
        listen 443 ssl;
        root /var/django/wbsrch/templates;
	access_log /var/django/wbsrch/log/access.log;
	error_log /var/django/wbsrch/log/error.log;
        gzip on;
        gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
        gzip_vary on;
        gzip_proxied any;

        ssl_certificate /etc/nginx/certs/wbsrch.crt;
        ssl_certificate_key /etc/nginx/certs/wbsrch.key;

        if ($ssl_protocol = "") {
            return 301 https:$host$request_uri;
        }

        location ~ ^/admin/static/ {
            root /home/xangis/.virtualenvs/wb/lib/python2.7/site-packages/django/contrib/;     
        }

        location /maintenance.htm {
            if (-f $document_root/maintenance.htm) {
                return 503;
           }
         }

        location ~* ^.+\.(jpg|jpeg|gif|css|png|js|ico|pdf|zip|exe|wav|gz|bmp|tgz|gz|rar|txt|tar|rtf|otf|ttf|html)$ {
            root /var/django/wbsrch/templates/;
            access_log off;
            expires 30d;
        }

        location / {
                include /etc/nginx/uwsgi_params;
                uwsgi_pass 127.0.0.1:9116;
                uwsgi_read_timeout 180;
        }

        error_page 502 503 =503 @maintenance;
        location @maintenance {
                rewrite ^(.*)$ /maintenance.htm break;
        }
}

