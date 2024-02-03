Below is a basic example of an Nginx configuration that meets some common requirements, such as serving a static website and using an alias to serve images from a different directory. Please adapt the paths and configurations according to your specific setup.

nginx
Copy code
server {
    listen 80;
    server_name your_domain.com;

    # Set the root directory for the main website
    root /var/www/html;

    # Index file and its extension
    index index.html;

    location / {
        # Additional configurations for the main website, if needed
        try_files $uri $uri/ =404;
    }

    location /images/ {
        # Serve images from a different directory using alias
        alias /path/to/your/image/directory/;
        # Additional configurations for serving images, if needed
    }

    # Additional server configurations can be added here

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }

    # Enable gzip compression for better performance
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    # Additional global configurations can be added here

    # Example SSL configuration (comment out if not using SSL)
    # listen 443 ssl;
    # ssl_certificate /etc/nginx/ssl/your_domain.crt;
    # ssl_certificate_key /etc/nginx/ssl/your_domain.key;
    # ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    # ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384';
    # ssl_prefer_server_ciphers on;

    # Additional SSL configurations can be added here
}
Remember to replace placeholders such as your_domain.com, /var/www/html, and /path/to/your/image/directory/ with your actual domain and directory paths. Additionally, consider enabling SSL by uncommenting the relevant lines if your site requires secure communication. After making changes, don't forget to restart or reload the Nginx service for the configuration to take effect.
