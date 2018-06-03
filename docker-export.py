import sh

data = sh.docker('ps')
docker_list = data.split('\n')[1].split(' ')[0].strip()
sh.docker('export',docker_list,"-o backup.tar.gz")