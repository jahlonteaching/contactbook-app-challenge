class Contact:
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.tags = []


    def add_tag(self, tag:str):
        if tag in self.tags:
            raise ValueError("Tag already exists")
        self.tags.append(tag)