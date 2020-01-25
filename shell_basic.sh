#!/bin/bash
# see
# https://www.cyberciti.biz/faq/bash-for-loop/

# space not permitted aroung equal(=)
a=''
for i in {1..5}
do
    echo "hello $i times"
    a=$a$i #character concatenation
done
echo "string $a"

# making a string from ascii code
# https://orebibou.com/2017/03/bash%E3%81%A7%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%82%92%E3%82%A2%E3%82%B9%E3%82%AD%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E8%A8%98%E8%BF%B0%E3%81%97%E3%81%A6%E5%AE%9F%E8%A1%8C%E3%81%95/
echo $'\x54\x55'
