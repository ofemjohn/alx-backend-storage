# 0x02. Redis basic

### REDIS INSTALLATION 
```
sudo apt-get -y install redis-server    # Install Redis server
pip3 install redis                     # Install Redis client library for Python
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf    # Update Redis configuration to bind only to the local interface
sudo systemctl restart redis           # Restart Redis to apply the new configuration
