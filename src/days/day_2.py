# requires version python 3.10 or greater

from src.common.library import elf_wise_data


def day_2() -> None:  # top three calories
    calories_data: dict[int: int] = elf_wise_data()
    calories_data_sorted: list[int] = sorted(calories_data.items(), key=lambda x: x[1], reverse=True)
    print(f"total of top three elves'  calories is {sum([cals for (_, cals) in calories_data_sorted[:3]])} \n")
    return


def main():
    day_2()
    return

if __name__ == '__main__':
    main()