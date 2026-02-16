from pathlib import Path
from sys import argv
from colorama import init, Fore # type: ignore


init(autoreset=True)


# Return object with cats information.
def dir_list(path: Path, depth: int = 0) -> None:
    if not path.exists():
        print(Fore.RED + f"Path {path} does not exist.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Path {path} is not a directory.")
        return
    dir_entries = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    for item in dir_entries:
        if item.is_dir():
            print(Fore.BLUE + f"{' ' * depth * 2}{path}/{item.name}")
            dir_list(item, depth + 1)
        else:
            print(Fore.GREEN + f"{' ' * depth * 2}{item.name}")


def main():
    start_path = argv[1] if len(argv) > 1 else "./"
    dir_list(Path(start_path))


if __name__ == "__main__":
    main()