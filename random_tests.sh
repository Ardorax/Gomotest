#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <number> first_bin secon_bin"
    exit 1
fi

num_files=$1
bin1=$2
bin2=$3

if [ ! -x $bin1 ]; then
    echo "$bin1 is not executable or does not exist."
    exit 1
fi

if [ ! -x $bin2 ]; then
    echo "$bin2 is not executable or does not exist."
    exit 1
fi

if [ ! -d tmp ]; then
    mkdir tmp
fi

for ((i=0; i<num_files; i++)); do
    python map_generator.py "tmp/map$i.txt"
    $bin1 "tmp/map$i.txt" > tmp1.txt
    $bin2 "tmp/map$i.txt" > tmp2.txt

    diff tmp1.txt tmp2.txt > /dev/null
    if [ $? -eq 0 ]; then
        continue
    fi

    echo -e "\033[1;38;5;160mDIFFERS\033[0m"
    while IFS= read -r line1 && IFS= read -r line2 <&3; do
        len1=${#line1}
        len2=${#line2}

        for ((i = 0; i < len1; i++)); do
            char1="${line1:i:1}"
            char2="${line2:i:1}"

            if [ "$char1" != "$char2" ]; then
                if [ "$char1" == "." ]; then
                    echo -ne "\033[30;41m1\033[0m"
                fi
                if [ "$char2" == "." ]; then
                    echo -ne "\033[30;43m2\033[0m"
                fi
            else
                echo -ne "$char1"
            fi
        done
        echo
    done < tmp1.txt 3< tmp2.txt
done

rm -f tmp1.txt tmp2.txt
rm -rf tmp
