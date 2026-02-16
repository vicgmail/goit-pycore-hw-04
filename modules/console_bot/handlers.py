from colorama import Fore # type: ignore

# Handler functions for each command
CONTACTS = {}


def hello():
    print("How can I help you?")


def show_all_contacts():
    for name, phone in CONTACTS.items():
        print(f"  {name}: {phone}")


def add_contact(args):
    if not args or len(args) < 2:
        print("Usage: add_contact <name> <phone_number>")
        return
    name = " ".join(args[:len(args)-1])
    phone = args[len(args)-1]
    CONTACTS[name] = phone
    print(f"Added contact {Fore.GREEN}{name}{Fore.RESET} with phone: {Fore.GREEN}{phone}{Fore.RESET}")


def change_contact(args):
    if not args or len(args) < 2:
        print("Usage: change_contact <name> <new_phone_number>")
        return
    name = " ".join(args[:len(args)-1])
    phone = args[len(args)-1]
    if name in CONTACTS:
        CONTACTS[name] = phone
        print(f"Changed contact {Fore.GREEN}{name}{Fore.RESET} to phone: {Fore.GREEN}{phone}{Fore.RESET}")
    else:
        print(f"Contact not found: {Fore.RED}{name}{Fore.RESET}")


def delete_contact(args):
    if not args:
        print("Usage: delete_contact <name>")
        return
    name = " ".join(args)
    if name in CONTACTS:
        del CONTACTS[name]
        print(f"Deleted contact: {Fore.GREEN}{name}{Fore.RESET}")
    else:
        print(f"Contact not found: {Fore.RED}{name}{Fore.RESET}")


def show_contact(args):
    if not args:
        print("Usage: show_contact <name>")
        return
    name = " ".join(args)
    if name in CONTACTS:
        print(f"{Fore.GREEN}{name}{Fore.RESET} has phone: {Fore.GREEN}{CONTACTS[name]}{Fore.RESET}")
    else:
        print(f"Contact not found: {Fore.RED}{name}{Fore.RESET}")