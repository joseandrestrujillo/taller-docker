
## Instalación

Instalar en [Debian](https://docs.docker.com/engine/install/debian/) [Windows](https://docs.docker.com/docker-for-windows/install/), [MacOS](https://docs.docker.com/docker-for-mac/install/).

  

## Docker

  

Para realizar la parte de docker ejecutar los siguientes comandos dentro de la carpeta ´/docker´

  

    docker build -t hola-docker:latest .
    docker run -p 8081:8080 hola-docker:latest


  Si no va el build ejecutar: 

  
    docker buildx build -t hola-docker:latest .
    docker run -p 8080:8080 hola-docker:latest



Abrir http://localhost:8080 en el navegador.

  

## Docker Compose

Para ejecutar el ejemplo con docker compose ejecutamos

    docker compose up --build



## Problemas frecuentes 

[Versiones antiguas](https://docs.docker.com/engine/install/ubuntu/)
[Permisos](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue)
