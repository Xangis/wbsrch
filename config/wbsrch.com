server {
	listen 80;
        listen 443 ssl;
	server_name www.wbsrch.com;
        ssl_certificate /etc/letsencrypt/live/wbsrch.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/wbsrch.com/privkey.pem;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers HIGH:!aNULL:!MD5;
	rewrite ^/(.*) https://wbsrch.com/$1 permanent;
	}

server {
	listen 80;
	server_name *.wbsrch.com wbsrch.com;
        listen 443 ssl;
        root /var/django/wbsrch/templates;
	access_log off;
	error_log off;
        gzip on;
        gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
        gzip_vary on;
        gzip_proxied any;
        client_max_body_size 2M;

        ssl_certificate /etc/letsencrypt/live/wbsrch.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/wbsrch.com/privkey.pem;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers HIGH:!aNULL:!MD5;

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

        location ~* ^.+\.(jpg|jpeg|gif|css|png|js|ico|pdf|zip|exe|wav|gz|bmp|tgz|gz|rar|txt|tar|rtf|otf|ttf|html|xml)$ {
            root /var/django/wbsrch/templates/;
            access_log off;
            expires 14d;
        }

        location / {
                include /etc/nginx/uwsgi_params;
                uwsgi_pass 127.0.0.1:9116;
                uwsgi_read_timeout 300;
        }

        error_page 502 503 =503 @maintenance;
        location @maintenance {
                rewrite ^(.*)$ /maintenance.htm break;
        }
}

