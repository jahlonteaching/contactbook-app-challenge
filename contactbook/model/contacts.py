from typing import List

class ContactBook:
    def __init__(self):
        self.contacts: dict[str, Contact] = {}

    def list_contacts(self)->List['Contact']:
        return list(self.contacts.values())

    def contacts_by_tag(self,tag:str)->List['Contact']:
        return [c for c in self.contacts.values() if tag in c.tags]

    def search_by_criteria(self,name:str = "",phone:str = "",email:str = ""):->List['Contact']:
        name= name.strip().lower()
        phone = phone.strip().lower()
        email = email.strip().lower()

        results:List['Contact'] = []
        for c in self.contacts.values():
            match = True
            if name and name not in c.name.lower():
                match = False
            if phone and phone not in c.phone.lower():
                match = False
            if email and email not in c.email.lower():
                match = False
            if match:
                results.append(c)
        return results