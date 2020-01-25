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


