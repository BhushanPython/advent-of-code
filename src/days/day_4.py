# Requires Version 3.10 or greater
import re


def read_day_4_data() -> list[str]:
    with open(r"../../data/day_4.dat", "r") as inp:
        assignment_pairs: list[str] = inp.readlines()
        assignment_pairs = [pair.strip() for pair in assignment_pairs]
    return assignment_pairs


def check_list_in_list(list1: list[int], list2: list[int]):  # check if either list of numbers is entirelu contained in the other
    return (list1[0] >= list2[0]) and (list1[-1] <= list2[-1]) or \
           (list2[0] >= list1[0]) and (list2[-1] <= list1[-1])


def check_list_overlap_list(list1: list[int], list2: list[int]):
    return list1[0] in list2 or list1[-1] in list2 or list2[0] in list1 or list2[-1] in list1


def day_4():
    inside_list_count: int = 0
    overlap_count: int = 0
    assignment_pairs: list[str] = read_day_4_data()
    for pairs in [re.split(",", pair) for pair in assignment_pairs]: # split in to elf1/ elf2
        elf1_range: str = pairs[0]  #
        elf1_range_list: list = re.split("-", elf1_range) # for elf split into start and end
        start = int(elf1_range_list[0])
        end = int(elf1_range_list[1])
        elf1_list = list(range(start, end + 1)) # use start and end to create a start to end list

        elf2_range: str = pairs[1]  # repeat for elf2
        elf2_range_list: list = re.split("-", elf2_range)
        start = int(elf2_range_list[0])
        end = int(elf2_range_list[1])
        elf2_list = list(range(start, end + 1))
        if check_list_in_list(elf1_list, elf2_list):
            inside_list_count += 1
        if check_list_overlap_list(elf1_list, elf2_list):
            overlap_count += 1
            print(f'{elf1_list} ******** {elf2_list}')
    print(inside_list_count, overlap_count)
    return


def main():
    day_4()
    return


if __name__ == '__main__':
    main()
