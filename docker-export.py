import sh

data = sh.docker('ps')
docker_list = data.split('\n')[1].split(' ')[0].strip()
print(sh.docker('stop',docker_list))
print(sh.docker('cp',docker_list+":/root/.android/avd/","/home/ubuntu/dockeravd"))
print(sh.tar('zcvf',"/home/ubuntu/dockeravd.tar.gz","/home/ubuntu/dockeravd"))
print(sh.tar('zcvf',"/home/ubuntu/dockeravd.tar.gz","/home/ubuntu/dockeravd"))