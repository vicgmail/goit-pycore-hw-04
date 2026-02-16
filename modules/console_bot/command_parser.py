import handlers
from colorama import Fore # type: ignore


AVAILABLE_COMMANDS = {
    "add": "Add a new contact", 
    "change": "Change an existing contact",
    "delete": "Delete a contact",
    "all": "Show all contacts",
    "phone": "Show a specific contact",
    "help": "Show available commands",
    "close": "Close the application",
    "hello": "Greet the user"
}


# Parse entered commands and execute corresponding actions
def command_parser(input_command: str) -> None:
    if not input_command.strip():
        return

    command_parts = input_command.split()
    command = command_parts[0].lower()
    args = command_parts[1:] if len(command_parts) > 1 else []

    if command not in AVAILABLE_COMMANDS:
        print(f"Invalid command: {Fore.RED}{command}{Fore.RESET}. Type 'help' for available commands.")
        return
    
    if command == "add":
        handlers.add_contact(args)
    elif command == "change":
        handlers.change_contact(args)
    elif command == "delete":
        handlers.delete_contact(args)
    elif command == "all":
        handlers.show_all_contacts()
    elif command == "phone":
        handlers.show_contact(args)
    elif command == "hello":
        handlers.hello()
    elif command == "help":
        print("Available commands:")
        for c, d in AVAILABLE_COMMANDS.items():
            print(f"  {Fore.GREEN}{c}{Fore.RESET}: \t{d}")
    
    return True
