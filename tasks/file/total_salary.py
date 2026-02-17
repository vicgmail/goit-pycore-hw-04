from pathlib import Path


# Calculates total, average salary of employees for a given file.
def total_salary(file: str) -> object:
    total = 0
    count = 0
    path = Path(file)
    if not path.exists() or not path.is_file():
        print(f"File {file} does not exist.")
        return (0, 0)
    
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            try:
                values = line.split(',')
                salary = float(values[1].strip())
                total += salary
                count += 1
            except ValueError:
                print(f"Invalid salary value: {values[1]} is not a number.")
                continue
    average = round(total / count, 2) if count > 0 else 0
    return (total, average)


def main():
    result = total_salary("./data/salary.txt")
    print(f"Total salary: {result[0]:.2f}")
    print(f"Average salary: {result[1]:.2f}")


if __name__ == "__main__":
    main()