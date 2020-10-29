echo Current Path: $PWD
echo Enter absolute path of config.json 
echo eg: $PWD
echo Enter it here: 
read varmain
echo Enter rb data
echo Unless you need to intentionally change it, it should be rb
echo Enter it here:
read varsecn
echo Enter what you named your primary storage file:
read varmisc
echo Enter what you named your secondary storage file:
read varothr
echo $varmain > $PWD/$varmisc
echo $varsecn > $PWD/$varothr
echo Done.
