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
	ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';
	ssl_prefer_server_ciphers on;
        ssl_dhparam /etc/nginx/dhparams.pem;

        if ($ssl_protocol = "") {
            return 301 https:$host$request_uri;
        }

        location ~ ^/admin/static/ {
            root /home/xangis/.virtualenvs/wbsrch/lib/python2.7/site-packages/django/contrib/;     
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

