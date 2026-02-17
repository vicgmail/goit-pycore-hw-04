from pathlib import Path


# Return object with cats information.
def get_cats_info(file: str) -> object:
    path = Path(file)
    if not path.exists() or not path.is_file():
        print(f"File {file} does not exist.")
        return []

    result = []
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            values = line.strip().split(',')
            if values[0]:
                result.append({
                    "id": values[0],
                    "name": values[1] if len(values) > 1 else "",
                    "age": values[2] if len(values) > 2 and values[2].isdigit() else "0"
                })

    return (result)


def main():
    result = get_cats_info("./data/cats.txt")
    print(f"Cats info: {result}")


if __name__ == "__main__":
    main()