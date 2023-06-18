# Alapvizsga
# Halozatok - Router/Switch config parancsok

enable
conf t
hostname
interface g 0/0
ip address 123.123.123.123 255.255.255.0
exit
no shutdown
line console 0
password asd
login
no login
line vty 0 15
telnet - távoli config
enable password
show running-config
enable secret
service password-encryption
crypto key generation
banner motd
banner login
ipv6 unicast-routing
show ip route
ip route 0.0.0.0 0.0.0.0 se0/0/1 192.168.1.0
copy startup-config tftp: 123.123.123.123
ip-domain domain.net
crypto key generate rsa




#Subnet maskok
/32 255.255.255.255
/31 255.255.255.254
/30 255.255.255.252
/29 255.255.255.248
/28 255.255.255.240
/27 255.255.255.224
/26 255.255.255.192
/25 255.255.255.128
/24 255.255.255.0
/23 255.255.254.0
/22 255.255.252.0
/21 255.255.248.0
/20 255.255.240.0
