while getopts a: flag
do
    case "${flag}" in
        a) arg=${OPTARG};;
    esac
done
variable=$(awk $arg tables.txt)
echo $variable
