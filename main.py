import server


counter = 0


def image_handler(image):
    global counter
    counter += 1
    return "This is a message written by the server. message number:" + str(counter)


def main():
    srvr = server.Server(image_handler)
    srvr.run()


if __name__ == "__main__":
    main()
