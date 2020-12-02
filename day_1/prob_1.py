from typing import List
import time


def calculate_sums(target: int):
    """
    Advent of Code, Problem 1: Given a list of integer inputs, find two values that sum to a given target value. For
    part two, find three values that sum to a given target value.
    """
    # Read the data file into a list
    data_list: List
    with open("prob_1_input.txt") as f:
        data_list = [int(line.rstrip('\n')) for line in f]

    # Part 1 - Find two complementary numbers
    for i, value in enumerate(data_list):
        # We're looking for complementary numbers, that is, numbers that add up to our target. For each value in the
        # provided dataset, find its complement, and then check to see if its present in the list
        complement: int = target - value

        # Check forward in the list of values for the complement. We've already checked any values prior to this one
        if complement in data_list[i+1:]:
            print(f"{value} + {complement} == 2020")
            print(f"Solution 1 (value * complement) = {value * complement}\n")
            break

    # Part 2 - Find three complementary numbers
    for i, value in enumerate(data_list):
        # We can continue to use the notion of complementary numbers. By summing the current number with the next number
        # and then finding the sums complement, we should be able to locate the proper complement. Unfortunately, for
        # the third complement, we have to scan the entire list

        # Keep track of whether we have a solve in the inner loop, this allows for a small performance boost
        solved: bool = False

        if (i + 1) < len(data_list):
            for k in data_list:
                partial_sum: int = value + k

                if partial_sum < target:
                    complement: int = target - partial_sum

                    # Now, just check forward in the list
                    if complement in data_list:
                        print(f"{value} + {k} + {complement} == 2020")
                        print(f"Solution 2 (value * k * complement) = {value * k * complement}\n")
                        solved = True
                        break
        if solved:
            break


if __name__ == "__main__":
    start = time.perf_counter()
    calculate_sums(target=2020)
    end = time.perf_counter()
    print(f"Finished in {end - start:0.4f} seconds")


