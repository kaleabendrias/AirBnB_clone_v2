#!/usr/bin/env bash
# Bash script that sets up your web servers

apt-get -y install nginx
if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create the fake html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data server to ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# change the config to server hbnb_static
nginx_config="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n}"
if ! grep -q "$nginx_alias" "$nginx_config"; then
    sudo sed -i "/server_name _;/a $nginx_alias" "$nginx_config"
fi

# Restart Nginx
sudo service nginx restart
