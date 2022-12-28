import ingest
import persist


class DriverProgram:
    def __int__(self, fileType):
        print("Inside Constructor")
        self.fileType = fileType

    def my_function(self):
        print("File Type =  " + self.fileType)


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    reader = ingest.FileReader()
    writer = persist.PersistData()
    reader.read_file()
    writer.store_data()
    driver = DriverProgram()
