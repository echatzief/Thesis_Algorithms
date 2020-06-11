#!/bin/bash

for number in {0..1..1}
do
  sudo timeout 100 tcpdump -i veth5d6ff2c  src 172.18.0.8 -w ./pcap_test/${number}.pcap 
done

python extract_features.py --type test
python test.py
