#!/bin/bash

for number in {0..1..1}
do
  sudo timeout 100 tcpdump -i veth3896f90 src 172.18.0.8 -w ./pcap_files/${number}.pcap 
done

python extract_features.py --type train
python3 train.py
