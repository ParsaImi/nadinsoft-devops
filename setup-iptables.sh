# Setup default policies
sudo iptables --policy INPUT DROP
sudo iptables --policy OUTPUT DROP
sudo iptables --policy FORWARD DROP

#Ratelimit SSH for attack protection
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -j ACCEPT

# Block external access to Prometheus (9091), Alertmanager (9095), Grafana (3000), Python Webapp (8000)
sudo iptables -A INPUT -p tcp -m tcp --dport 8000 -j DROP
sudo iptables -A INPUT -p tcp -m tcp --dport 9091 -j DROP
sudo iptables -A INPUT -p tcp -m tcp --dport 9095 -j DROP
sudo iptables -A INPUT -p tcp -m tcp --dport 3000 -j DROP


# Allow pinging of your server
sudo iptables -A INPUT -p icmp --icmp-type 8 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

# Drop all other traffic
sudo iptables -A INPUT -j DROP

sudo iptables -nL

