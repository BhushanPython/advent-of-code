# requires Python 3.10 or greater

def get_common_items_total(items_data: list[str], place_values: dict[chr: int]) -> int:
    total: int = 0
    for string_of_items in items_data:
        string_of_items = string_of_items.strip()
        if len(string_of_items) % 2 != 0:
            raise TypeError(f'Need to have even number of characters. Not true for {string_of_items} \n')
        else:
            part_1 = string_of_items[: len(string_of_items)//2]
            part_2 = string_of_items[len(string_of_items)//2:]
            common_items: list[chr] = [char for char in part_1 if char in part_2]
            common_items = list(set(common_items))  # remove repetitions
            total += sum([place_values[char] for char in common_items])
    return total


def get_place_values() -> dict[chr: int]:
    place_values = {}
    for (p, c) in enumerate([chr(x) for x in list(range(ord('a'), ord('z') + 1))]):
        place_values[c] = p + 1
    for (p, c) in enumerate([chr(x) for x in list(range(ord('A'), ord('Z') + 1))]):
        place_values[c] = p + + 1 + place_values['z']
    return place_values


def day_3() -> None:
    place_values: dict[chr: int] = get_place_values()
    with open(r'../data/day_3.dat', "r") as input_file:
        items_data: list[str] = input_file.readlines()
    total: int = get_common_items_total(items_data=items_data, place_values=place_values)
    print(f"Total is {total} \n")
    return


def main():
    day_3()
    return


if __name__ == '__main__':
    main()