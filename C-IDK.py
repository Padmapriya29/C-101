import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A9_O07jyJ0NqnGSWJGiegJmwBgLVEWn3OXFg5VXpHVpLOSlJ11_hPke_adJsCpnKL7jd2baNMUQyXOgU8yqgzb8gR2YPzEV00o0-ITEc2jD6pbnVdEaVzQh_G3gNqwJyzKdN5ao'
    transferData = TransferData(access_token)

    file_from = input("E:\WhiteHatJunior\C101\Padmpriya2008")
    file_to = input("E:\WhiteHatJunior\C101\C-IDK")

    transferData.upload_files(file_from, file_to)
    print("just a sample")

    main()