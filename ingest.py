class FileReader:
    def __init__(self, fileType):
        print("Constructor for File Reader")
        self.fileType = fileType

    def read_file(self):
        print("Reading - " + self.fileType + " file")
