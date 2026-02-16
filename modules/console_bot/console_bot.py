from command_parser import command_parser


def main():
    while True:
        command = input("Enter a command (type 'exit' to quit): ").lower().strip()
        if command == "exit" or command == "close":
            break
        else:
            command_parser(command)


if __name__ == "__main__":
    main()