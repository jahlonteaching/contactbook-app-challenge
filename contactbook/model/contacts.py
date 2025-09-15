from datetime import datetime

class Contact:
    def __init__(self, name: str, phone: str, email: str,):
        self.name = name
        self.phone = phone
        self.email = email
        self.tags: list[str] = []
        self.creation_date: datetime = datetime.now()


    def add_tag(self, tag:str):
        if tag in self.tags:
            raise ValueError("Tag already exists")
        self.tags.append(tag)

    def __str__(self) -> str:
        return (f"Name: {self.name}\n,"
                f"Phone: {self.phone}\n,"
                f"Email: {self.email}\n,"
                f"Tags: {self.tags}\n,"
                f"Created on: {self.creation_date}")