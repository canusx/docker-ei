import sh

data = sh.docker('ps')
docker_list = data.split('\n')[1].split(' ')[0].strip()
print(sh.docker('stop',docker_list))
print(sh.docker('cp',"/home/ubuntu/entrypoint.sh",docker_list+":/"))
print(sh.docker('start',docker_list))