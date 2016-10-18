# Copyright 2016 django-tasix authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from netaddr import IPAddress, IPNetwork

IP_RANGE = [
    "217.30.160.0/20", "217.29.112.0/20", "217.12.86.0/24",
    "217.12.84.0/23", "217.12.80.0/22", "213.230.64.0/18",
    "213.206.32.0/19", "195.238.104.0/22", "195.211.180.0/22",
    "195.158.0.0/19", "195.88.214.0/23", "193.27.206.0/23",
    "188.130.255.0/24", "188.130.172.0/24", "188.113.192.0/18",
    "185.163.24.0/22", "185.139.136.0/22", "185.78.136.0/22",
    "185.74.100.0/22", "185.74.4.0/22", "185.63.224.0/22",
    "185.8.212.0/23", "185.6.40.0/22", "185.4.160.0/22",
    "178.218.200.0/21", "178.216.128.0/21", "146.120.16.0/22",
    "109.248.220.0/23", "109.207.240.0/20", "95.46.80.0/20",
    "95.46.64.0/21", "94.230.224.0/20", "94.158.48.0/20",
    "94.141.64.0/19", "92.223.99.0/24", "92.38.52.0/22",
    "92.38.24.0/22", "91.240.12.0/22", "91.234.218.0/23",
    "91.231.56.0/22", "91.229.164.0/23", "91.229.160.0/22",
    "91.213.31.0/24", "91.212.180.0/24", "91.212.89.0/24",
    "91.204.236.0/22", "91.203.172.0/22", "91.196.76.0/22",
    "91.188.128.0/19", "89.236.192.0/18", "89.146.64.0/18",
    "87.237.232.0/21", "84.54.120.0/22", "84.54.114.0/24",
    "84.54.112.0/23", "84.54.96.0/20", "84.54.64.0/19",
    "83.221.176.0/20", "83.221.168.0/21", "83.221.164.0/22",
    "83.221.163.0/24", "83.221.160.0/23", "83.69.128.0/19",
    "82.215.88.0/22", "82.215.80.0/21", "82.215.72.0/21",
    "82.215.68.0/22", "82.215.66.0/23", "82.215.65.0/24",
    "81.95.224.0/20", "80.80.208.0/20", "77.220.192.0/19",
    "62.209.128.0/19", "46.255.64.0/21", "46.227.120.0/21",
    "46.8.35.0/24", "37.110.208.0/21", "31.135.208.0/21",
    "31.40.24.0/22"
]

NETWORK = [ IPNetwork(ip_range) for ip_range in IP_RANGE ]

def is_tasix_member(ip_address):
    for ip_range in NETWORK:
        if IPAddress(ip_address) in ip_range:
            return True
