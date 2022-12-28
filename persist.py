class PersistData:

    def __init__(self, dbType):
        self.dbType = dbType

    def store_data(self):
        print("Storing Data to "+self.dbType)