from wsgiref.simple_server import make_server

PORT = 3000
HTML = """
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <h1>Hello from simple server {{username}}!</h1>
    <p>Do something in here!!</p>
    <p>Código</p>
  </body>
</html>
"""
def application(environ, start_response):  # WSGI Interface
  status = '200 ok'
  headers = []
  params = str(environ.get('QUERY_STRING'))
  username = params.split('=')[1]
  render = HTML.replace("{{username}}", username)

  start_response(status, headers)  # Metadata

  return [bytes(render, 'utf-8')]  # Response to the client


with make_server('127.0.0.1', PORT, application) as server:
  print(f">>> The server is listening on port {PORT}")
  server.serve_forever()