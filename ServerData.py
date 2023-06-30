class ServerData:
    data = ""

    def __init__(self, data):
        self.data = data

    def insert_data(self, data):
        self.data = data

    def get_data(self):
        print(self.data)
        return self.data
