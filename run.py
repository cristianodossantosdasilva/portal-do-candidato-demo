import http.server
import socketserver
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).resolve().parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as server:
    print(f"Portal disponível em http://127.0.0.1:{PORT}")
    print("Pressione Ctrl+C para encerrar.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")

