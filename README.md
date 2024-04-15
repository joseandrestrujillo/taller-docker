## Instalación

Actualizamos el sistema
´´´bash
sudo apt update
´´´
Instalamos Docker
´´´bash
sudo apt install docker.io
´´´
Verificamos la descarga
´´´bash
sudo docker run hello-world
´´´
Instalar en [Windows](https://docs.docker.com/docker-for-windows/install/), [MacOS](https://docs.docker.com/docker-for-mac/install/).

## Docker

Para realizar la parte de docker ejecutar los siguientes comandos dentro de la carpeta ´/docker´

´´´
docker build -t hola-docker:latest .
docker run -p 8080:8080 hola-docker:latest
´´´

Abrir http://localhost:8080 en el navegador.

## Docker Compose
Para ejecutar el ejemplo con docker compose ejecutamos
´´´bash
docker compose up --build
´´´