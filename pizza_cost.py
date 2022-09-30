#!/usr/bin/env python3

# Created By: Jessah
# Date: Sept 30, 2022
# This program calculates the pizza cost.

import constants


def main():
    # input
    print()
    diameter = int(input("Enter the diameter of the pizza: "))

    # process

    subtotal = constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output
    print()
    print("The total cost of the pizza is: ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
