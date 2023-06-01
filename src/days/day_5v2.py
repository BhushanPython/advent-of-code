from dataclasses import dataclass
import re


@dataclass
class Move:
    source: int
    dest: int
    num: int


class Stack:
    def __init__(self, stack_num: int):
        self.stack_num = stack_num
        self.crates: list[chr] = []
        return

    def remove_crate(self) -> chr:
        return self.crates.pop()

    def add_crate(self, crate: chr) -> None:
        self.crates.append(crate)
        return


max_stack_height: int = 8
col_data_width: int = 4
num_stacks: int = 9
stacks: {int: Stack} = {}


def print_stack(stack: Stack) -> None:
    print(f"Stack Num is: {stack.stack_num} and crates is {stack.crates}")
    return


def print_all_stacks(stacks: {int: Stack}) -> None:
    for stack in stacks.values():
        print_stack(stack)
    return


def parse_line(line: str) -> list[chr]:
    crates: list[chr] = []
    for stack_num in range(1, num_stacks + 1):
        crate = line[col_data_width * (stack_num - 1): col_data_width * (stack_num - 1) + col_data_width + 1]
        if crate is not None:
            crate = crate.strip('[] ')
            if crate is not None and len(crate) == 0:
                crate = None
            elif not ('A' <= crate <= 'Z'):
                raise ValueError(f'Incorrect crate name in line {line}, crate name {crate}')
        crates.append(crate)
    return crates


def update_stacks(crates: list[chr]) -> None:
    for stack_num, crate in [(pos + 1, val) for pos, val in enumerate(crates)]:
        if crate is not None:
            stacks[stack_num].add_crate(crate)
    return


def load_starting_positions() -> None:
    lines: list[str] = []
    with open(r"../../data/day_5.dat", "r") as inp_file:
        data = inp_file.readlines()
        for line in data[:8]:
            line = line.strip("\n")
            if line.strip() is None:
                pass
            else:
                lines.append(line)

    lines.reverse()
    for line in lines:
        crates = parse_line(line)
        if len(crates) != num_stacks:
            raise ValueError(f'Incorrect data for crates {crates}')
        update_stacks(crates)
    return


def get_moves() -> list[Move]:
    moves: list[Move] = []
    line_count: int = 0
    with open(r"../../data/day_5.dat", "r") as inp_file:
        while True:
            line = inp_file.readline().strip()
            if line_count > 10 and (line is None or len(line)) == 0:
                return moves
            elif 'move' not in line:
                pass
            else:
                data = re.findall(r'\d+', line)
                if len(data) != 3:
                    raise ValueError(f'Expect exactly three numbers. String is {line} and data is {data}')
                else:
                    moves.append(Move(source=int(data[1]), dest=int(data[2]), num=int(data[0])))
                line_count += 1
    return moves


def process_move(move: Move):
    source_stack = stacks[move.source]
    dest_stack = stacks[move.dest]
    for num_crates in range(move.num):
        crate = source_stack.remove_crate()
        dest_stack.add_crate(crate)
    return


def main():
    global stacks
    for stack_num in range(1, num_stacks + 1):
        stacks[stack_num] = Stack(stack_num=stack_num)
    load_starting_positions()
    print("Starting positions...")
    print_all_stacks(stacks)
    for move in get_moves():
        process_move(move)
    print("Final positions...")
    print_all_stacks(stacks)
    return


if __name__ == '__main__':
    main()
