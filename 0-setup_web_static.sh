#!/usr/bin env bash
# Stes up my web servers for web_static deployment

echo -e "\e[1;32m Packages updated\e[0m"
echo

#---Configure Firewall
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Allow incoming NGINX HTTP connetions\e[0m"
echo

#--Create the directory
sudo mkdir -p /data/web_static/releases/est /data/web_static/shared
echo -e "\e[1;32m directories created"
echo

#--add test string
echo "<h1>Welcome to www.chepkorir.tech</h1>" > /data/web_static/releases/test/index.html
echo -e "\e[1;32m Test string added\e[0m"
echo

#--Prevent overwrite
if [ -d "/data/web_static/current"];
then
	echo "path /data/web_static/current exists"
	sudo rm -rf /data/web_static/current;
fi;
echo -e "\e[1;32m prevent overwrite\e[0m"
echo

#--create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo ln -sf 'etc/nginx/sites-available/default' '/etc/nginx/sites-enable/default'
echo -e "\e[1;32m Symbolic link created\e[0m"
echo

#--restart NGINX
sudo service nginx restart
echo -e "\e[1;32m Restart NGINX\e[0m"
