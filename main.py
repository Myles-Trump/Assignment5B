#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program uses a while loop to solve the power of ever number
#   up to the inputted number


def main():
    # this function uses a while loop to solve the power of ever number
    #   up to the inputted number

    # this is to keep looping infinitely
    loop_counter = 0
    loop_counter_2 = 1

    # this is to set the default states for how many of each type there is
    positive = 0
    negative = 0
    zero = 0

    # input
    print("\n", end="")

    # process & output
    try:
        print("\n", end="")
        while loop_counter < loop_counter_2:
            print("Enter a positive, negative or zero.", end="")
            integer = input(" Enter Done when done (case sensitive): ")

            # finds a keyword in a string, found at
            #   https://pythonbasics.org/string-find/
            if "Done" in integer:
                break

            else:
                integer_int = int(integer)

                if integer_int > 0:
                    positive = positive + 1

                elif integer_int < 0:
                    negative = negative + 1

                else:
                    zero = zero + 1

        print("\nYou have {0} positives, {1} negatives and {2} zeros."
              .format(positive, negative, zero))

    except Exception:
        print("\nYou have entered an invalid input.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
