usage(){
    echo "usage: sh server.sh [-e environment --ini file]"
}

# SET environmental variable
ENV=

if [ $# -gt 0 ]; then
    while [ "$1" != "" ]; do
        case $1 in
            -e | --env )
                shift
                ENV=$1
                ;;
            -h | --help )
                usage
                exit
                ;;
            --ini )
                shift
                file=$1
                ;;
            * )
                usage
                exit 1
        esac
        shift
    done
else 
    usage
    exit 1
fi

# Activates Environment
export ENV
. venv/bin/activate

# Run server
uwsgi --ini "$file"