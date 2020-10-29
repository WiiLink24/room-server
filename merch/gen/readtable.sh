while getopts a: flag
do
    case "${flag}" in
        a) arg=${OPTARG};;
    esac
done
variable=$(awk $arg file)
echo $variable
