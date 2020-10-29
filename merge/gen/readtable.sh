grep -hnrq --no-messages $datamain $PWD/tables.txt > tmp.txt
datasecn=`cat tmp.txt`
echo $datasecn
rm -f tmp.txt
