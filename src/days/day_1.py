# requires version python 3.10 or greater
from src.common.library import elf_wise_data

def day_1() -> None:  # top calories
    calories_data: dict[int: int] = elf_wise_data()
    if len(calories_data) > 0:
        max_cals: int = max(calories_data.values())
        which_elf: int = [(num, cals) for (num, cals) in calories_data.items() if cals == max_cals][0][0]
        # above code assumes only one max candidate, therefore selects the first elf whose total matches max cals
    else:
        assert "Found no elves. Exiting.. \n"
    print(f"Max Calories is {max_cals} and is with elf {which_elf} \n")
    return


def main():
    day_1()
    return


if __name__ == '__main__':
    main()
