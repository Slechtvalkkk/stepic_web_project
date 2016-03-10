sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn ask.wsgi:application --bind 0.0.0.0:8000