import server


def image_handler(image):
    return "This is a message written by the server."


def main():
    srvr = server.Server(image_handler)
    srvr.run()


if __name__ == "__main__":
    main()
