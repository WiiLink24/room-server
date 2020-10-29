echo Current Path: $PWD
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
echo Exiting in 5...
sleep 1  # Waits 5 seconds.
echo Exiting in 4...
sleep 1  # Waits 5 seconds.
echo Exiting in 3...
sleep 1  # Waits 5 seconds.
echo Exiting in 2...
sleep 1  # Waits 5 seconds.
echo Exiting in 1...
sleep 1  # Waits 5 seconds.
