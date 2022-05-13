#!/bin/bash
# see
# https://www.cyberciti.biz/faq/bash-for-loop/

# for debug, just run a script with:
# bash -x [script]

# space not permitted aroung equal(=)
a=''
for i in {1..5}
do
    echo "hello $i times"
    a=$a$i #character concatenation
    # file creation
    echo "hello" > tmpfile$i.txt
done
echo "string $a"
ls tmpfile*
rm tmpfile*

# making a string from ascii code
# https://orebibou.com/2017/03/bash%E3%81%A7%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%82%92%E3%82%A2%E3%82%B9%E3%82%AD%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89%E3%81%A7%E8%A8%98%E8%BF%B0%E3%81%97%E3%81%A6%E5%AE%9F%E8%A1%8C%E3%81%95/
echo $'\x54\x55'

# awk basic
h='hello world'
echo $h | awk '{print $0}' # hello world
echo $h | awk '{print $1}' # hello
echo $h | awk '{print $2}' # world

hc='hello,world'
#specify separating character by -F option
echo $hc | awk -F',' '{print $1}'

# OS version check (16.04.6 is taken to be 16.046)
grep -i version /etc/os-release | sed 's/[^0-9.]//g' | awk '$1>16{print $1}'

# read file; $# is the number of argument (see StackOverFlow6482377)
if [ $# -eq 0 ]
then
    echo 'No argument'
else
    # array in bash (variable type can be specified by declare)
    declare -a string_list
    # while read line ('line' can be replaced by any variable)
    # is a standard usage
    # done < $1 means this loop reads text from the file of 1st argument
    # https://shellscript.sunone.me/while.html
    while read l
    do
	# if the initial word in a line containing lower case alphabet,
	# the word will be appended to string_list.
	a=$(echo $l | awk '{if($1 ~ /[a-z]/) print $1}')
	string_list+=($a)
    done < $1
    echo ${#string_list[@]} # the number of element in string_list
    echo ${string_list[@]} # all elements concatenated
fi

# reduce line feed
if [ $# -eq 0 ]
then
    echo 'No argument'
else
    out=''
    counter=1
    while read line
    do
	out=$out$line
	if (($counter % 7 == 0))
	then
	    echo $out
	    out=''
	fi
	counter=$((counter+1))
    done < $1
fi

# glibc version
ldd --version

# list only for directory
ls -l | grep '^d'

# temporary files (removed on script's end)
echo '---- demo of temporary file ---'
TMP1=`mktemp`
echo 'aaa' > $TMP1
TMP2=`mktemp`
echo 'bbb' > $TMP2
diff $TMP1 $TMP2
echo

# overwrite a bash command in .bashrc
# https://stackoverflow.com/questions/25399079/how-to-overwrite-a-bash-command
function echo() {
    command echo 'hello' $1;
}

# line by line PATH listing
# https://askubuntu.com/questions/600018/how-to-display-the-paths-in-path-separately
echo $PATH | tr ':' '\n'

# to see the number of cpu core:
nproc
cat /proc/cpuinfo
cat /proc/version # linux kernel version
uname -r # uname prints system info

# show only specified lines in a file: 57-60th lines here
sed -n 57,60p shell_basic.sh

# replace parameter value by sed
# https://stackoverflow.com/questions/11245144/replace-whole-line-containing-a-string-using-sed
# https://stackoverflow.com/questions/11146098/use-a-variable-in-a-sed-command
echo '\n---replace parameter value by sed---'
UPTIME=`cat /proc/uptime`
sed "s/^VERSION.*/VERSION=$UPTIME;/g" /etc/os-release

# to find subdirectories which consume disk
du -a . | sort -n -r | head -n 50

