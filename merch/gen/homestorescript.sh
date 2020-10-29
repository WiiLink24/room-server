while getopts a: flag
do
    case "${flag}" in
        a) arg=${OPTARG};;
    esac
done
useradd -m -p $arg store
echo Created user with $arg password
cp -r -a $PWD/home/store. /home/store
echo Install done.
