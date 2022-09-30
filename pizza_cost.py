#!/usr/bin/env python3

# Created By: Jessah
# Date: Sept 30, 2022
# This program calculates the pizza cost.

HST = 0.13
LABOUR_COST = 2.00
RENTAL_COST = 2.25
INGRED_COST = 1.50


def main():
    # input
    print()
    diameter = int(input("Enter the diameter of the pizza: "))

    # process

    subtotal = LABOUR_COST + RENTAL_COST + INGRED_COST * diameter
    tax = HST * subtotal
    total = subtotal + tax

    # output
    print()
    print("The total cost of the pizza is: ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
