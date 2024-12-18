def parse_input(file_path: str):
    """
    Reads the puzzle input from a file and returns two lists:
    one for the 'left' numbers and one for the 'right' numbers.

    :param file_path: Path to the input text file.
    :return: A tuple of two lists (left_list, right_list).
    """
    left_list = []
    right_list = []

    with open(file_path, 'r') as f:
        for line in f:
            left_str, right_str = line.split('\t')
            left_list.append(int(left_str))
            right_list.append(int(right_str))

    return left_list, right_list


def sort_lists(left_list, right_list):
    """
    Sorts the two lists in ascending order.

    :param left_list: List of integers (the 'left' list).
    :param right_list: List of integers (the 'right' list).
    :return: A tuple of two sorted lists (sorted_left, sorted_right).
    """
    pass


def solve_part_one(left_list, right_list):
    """
    Computes the total distance between the two lists after they are sorted.
    (Distance is defined as the absolute difference of paired elements, summed up.)

    :param left_list: List of integers (the 'left' list).
    :param right_list: List of integers (the 'right' list).
    :return: The total distance as an integer.
    """
    # Placeholder logic:
    # 1. Sort both lists.
    # 2. Pair each element from the sorted left list with the corresponding
    #    element from the sorted right list.
    # 3. Sum up the absolute differences.
    total_distance = 0
    # Example steps (commented out):
    # sorted_left = sorted(left_list)
    # sorted_right = sorted(right_list)
    # for i in range(len(sorted_left)):
    #     total_distance += abs(sorted_left[i] - sorted_right[i])

    return total_distance


def solve_part_two(left_list, right_list):
    """
    Placeholder for Part Two of the puzzle (the second half, which locks until Part One is completed).

    :param left_list: List of integers (the 'left' list).
    :param right_list: List of integers (the 'right' list).
    :return: Placeholder return value for Part Two.
    """
    # Placeholder logic. This will be defined when you unlock Part Two's challenge.
    result = None
    return result


def main():
    """
    Main function to tie everything together:
    1. Parse the input.
    2. Solve Part One (and print/store the result).
    3. Solve Part Two (and print/store the result), once its requirements are known.
    """
    input_file = "input.txt"  # Update if needed
    left_list, right_list = parse_input(input_file)

    part_one_answer = solve_part_one(left_list, right_list)
    print(f"Part One Answer: {part_one_answer}")

    # Part Two can be called after Part One is solved (or once the puzzle is unlocked)
    # part_two_answer = solve_part_two(left_list, right_list)
    # print(f"Part Two Answer: {part_two_answer}")


if __name__ == "__main__":
    main()
