import threading
import socket


class Server:

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, image_handler, port=8080, buffer_size=1024):
        self._image_handler = image_handler
        self._buffer_size = buffer_size
        self._port = port

        self._connections = []
        self.socket.bind(("0.0.0.0", self._port))
        self.socket.listen(1)
        print("server is listening at port", self._port)

    def handler(self, client_socket, address):
        active = True
        while active:
            image = client_socket.recv(self._buffer_size)
            if image:
                text = self._image_handler(image)
                print("client at address " + address + " sent an image.")
                text = text + "\n"
                client_socket.send(text.encode())
                print("sending client the text: " + text)
            else:
                print("client at address " + address + " disconnected.")
                active = False

    def run(self):
        while True:
            client_socket, address = self.socket.accept()
            address = address[0]

            client_thread = threading.Thread(target=self.handler, args=(client_socket, address))
            client_thread.daemon = True
            client_thread.start()

            self._connections.append(address)
            print("added client at IP: " + address)

    def get_connections(self):
        return self._connections

    def get_buffer_size(self):
        return self._buffer_size

    def get_port(self):
        return self._port
