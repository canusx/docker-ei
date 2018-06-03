import sh

data = sh.docker('ps')
docker_list = data.split('\n')[1].split(' ')[0].strip()
sh.docker('cp',docker_list+":/root/.android/avd/ /home/ubuntu/dockeravd")