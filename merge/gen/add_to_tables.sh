echo Enter the unique ID you placed into create.sh:
read varmain
echo Where is the python file located on this server that loads it?:
read varsecn
echo \n$varmain > $varsecn/tables.txt
