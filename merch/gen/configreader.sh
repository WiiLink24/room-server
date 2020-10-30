while getopts a:b: flag
do
    case "${flag}" in
        a) argmain=${OPTARG};;
        b) argsecn=${OPTARG};;
    esac
done
variable=$(awk $argmain $argsecn)
echo $variable
