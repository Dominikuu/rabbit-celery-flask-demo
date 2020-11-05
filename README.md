Start, stop, delete
```
#stop all containers:
docker kill $(docker ps -q) &&  docker rm $(docker ps -a -q) && docker rmi $(docker images -q)

remove all containers
docker rm $(docker ps -a -q)

remove all docker images
docker rmi $(docker images -q)
```