import my_dropbox


def main():
    # specify the token
    token = ''
    dbx = my_dropbox.Dropbox(token)
    # dbx.upload(path, filename)
    # dbx.download(path, filename)
    # ...


if __name__ == '__main__':
    main()
