# Dockerized flask-rabbit-celery app

A simple **Flask** application using RabbitMQ, Redis, Celery

## Get started

### Installing

To build application docker image,
```
docker-compose up --build
```
### Docker-compose

- RabbitMQ
- Celery
- Flask

```
version: '3'
services:
  rabbit:
    image: rabbitmq:latest
    environment:
      - RABBITMQ_DEFAULT_USER=admin
      - RABBITMQ_DEFAULT_PASS=admin-pass
    ports:
      - "5672:5672"

  worker:
    build: .
    entrypoint: ["celery"] # overriding the command in the Dockerfile
    command: ["worker", "-A", "app.worker", "--loglevel=info"]
    depends_on:
      - rabbit

  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - rabbit
  ```

### Operation of docker
Start, stop, delete
```
#stop all containers:
docker kill $(docker ps -q) &&  docker rm $(docker ps -a -q) && docker rmi $(docker images -q)

remove all containers
docker rm $(docker ps -a -q)

remove all docker images
docker rmi $(docker images -q)
```
