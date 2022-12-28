import ingest
import persist


class DriverProgram:
    def __init__(self, fileType):
        print("Inside Driver Constructor")
        self.fileType = fileType

    def my_function(self):
        print("File Type =  " + self.fileType)
        reader = ingest.FileReader(self.fileType)
        writer = persist.PersistData("postgres")
        reader.read_file()
        writer.store_data()


if __name__ == '__main__':
    driver = DriverProgram("csv")
    driver.my_function()
