from  dataclasses import dataclass, field

@dataclass
class ContactBook:
    def __init__(self, contacts: dict [str, Contacts]):
        self.contacts: dict[str, Contacts] = field(default_factory=dict)



    def add_contact(self, name, phone, email, tags):
        if phone in self.contacts:
            return False

        new_contact = self.contacts[phone]
        self.Contacts[phone] = new_contact


    def delete_contact(self, phone):
        if phone in self.contacts:
            removed_contact = self.contacts.pop(phone)
            print(f"  Contacto '{removed_contact.name}' con teléfono {phone} eliminado")
            return True
        else:
            print(f" No se encontró contacto con teléfono {phone}")
            return False


