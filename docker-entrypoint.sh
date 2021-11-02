#!/usr/bin/env sh

while true; do
  python cfddns.py;
  sleep ${TTL};
done
