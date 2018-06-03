import sh

data = sh.docker('ps')
docker_list = data.split('\n')[1].split(' ')[0].strip()
print(sh.docker('stop',docker_list))
print(sh.tar('zxf',"/home/ubuntu/dockeravd.tar.gz"))
print(sh.docker('cp',"/home/ubuntu/home/ubuntu/dockeravd/*",docker_list+":/root/.android/avd/"))
