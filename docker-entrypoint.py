import sh

data = sh.docker('ps')
print(sh.docker('stop',"android"))
print(sh.docker('cp',"/home/ubuntu/entrypoint.sh","android:/"))
print(sh.docker('start',"android"))