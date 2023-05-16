class Location:
    name = ""
    address = ""
    zip = ""
    language = ""
    def __init__(self, name, address, zip_code, language):
        self.name = name;
        self.address = address
        self.zip = zip_code
        self.language = language
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_zip(self):
        return self.zip

    def get_language(self):
        return self.language
