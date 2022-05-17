import dropbox


class Dropbox:

    token = ""
    dbx = None
    MAX_SPACE = 2147483648

    def __init__(self, token):
        self.token = token
        self.dbx = dropbox.Dropbox(self.token)

    def upload(self, path, filename):
        try:
            with open(path+"/"+filename, "rb") as f:
                self.dbx.files_upload(
                    f.read(), '/{}'.format(filename), mute=True)
            print("File uploaded")
        except Exception as e:
            print("An error occurred, file not uploaded:{}".format(e))

    def download(self, path, filename):
        try:
            self.dbx.files_download_to_file(
                path+"/"+filename, '/{}'.format(filename))
            print("File downloaded")
        except Exception as e:
            print("An error occurred, file not downloaded:{}".format(e))

    def get_user_info(self):
        return self.dbx.users_get_current_account()

    def get_user_space_info(self):
        return self.dbx.users_get_space_usage()

    def is_space_left(self):
        return self.dbx.users_get_space_usage().used == self.MAX_SPACE

    def get_used_space(self):
        return self.dbx.users_get_space_usage().used

    def delete_file(self, path):
        if self.isExists(path):
            self.dbx.files_delete_v2(path, parent_rev=None)
            print("File deleted")

    def exists_file(self, file):
        try:
            self.dbx.files_get_metadata(file)
            return True
        except:
            return False
