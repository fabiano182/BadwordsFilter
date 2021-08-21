#!/bin/bash

ifconfig enp0s3:0 192.168.100.10
ifconfig enp0s3:0 netmask 255.255.255.0

ifconfig enp0s3:1 192.168.100.11
ifconfig enp0s3:1 netmask 255.255.255.0
