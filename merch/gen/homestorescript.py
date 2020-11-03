import os
os.system('echo Current Path: $PWD')
os.system('variable=$(python3 password.py)')
os.system('useradd -m -p $arg store')
os.system('echo Created user with $arg password')
os.system('cp -r -a $PWD/home/store. /home/store')
os.system('echo Install done.')
