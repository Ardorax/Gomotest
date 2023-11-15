if [ -z "$1" ]; then
    echo "Usage: $0 <path to the brain>"
    exit 1
fi

: | { "$1" | ./main.py; } > /dev/fd/0