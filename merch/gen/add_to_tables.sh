echo Enter the unique ID you want:
read varmain
echo Where is the python file located on this server that loads it?:
read varsecn
echo What do you want the primary storage file to be named?:
read varothr
echo What do you want the secondary storage file to be named?:
read varrest
echo \n$varmain\n$varothr\n$varrest > $varsecn/tables.txt
echo $varmain > $varsecn/id.txt
