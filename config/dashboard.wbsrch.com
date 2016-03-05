upstream rd_servers {
  server 127.0.0.1:5000;
}
 
server {
  listen 80 default;
  server_name 52.33.32.115;
  rewrite https://wbsrch.com permanent;
}

server {
  listen 80;
  server_name dashboard.wbsrch.com;
  listen 443 ssl;

  ssl_certificate /etc/nginx/certs/wbsrch.crt;
  ssl_certificate_key /etc/nginx/certs/wbsrch.key;

  if ($ssl_protocol = "") {
      return 301 https:$host$request_uri;
  }
 
  access_log /var/log/nginx/rd.access.log;
 
  gzip on;
  gzip_types *;
  gzip_proxied any;
 
  location / {
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass       http://rd_servers;
  }
}
