#! /bin/bash
cat payload.txt | while read LINE; do
    echo $LINE | python3 aes.py
done
