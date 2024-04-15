from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola desde Docker</title>
    <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body>
    <div class="container mx-auto py-12 text-center">
        <h1 class="text-3xl font-bold text-center mb-4">Hola desde Docker</h1>
        <p class="text-gray-600 text-lg">Este es un ejemplo de un servidor web simple que se ejecuta en un contenedor Docker.</p>
    </div>
    </body>
    </html>
    """

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
