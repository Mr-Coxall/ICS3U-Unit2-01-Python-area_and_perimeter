#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2020
# This program calculates the area and perimeter of a circle
#    with radius 5cm

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 5cm: ")
    print("")
    print("Area is {}cm².".format(math.pi * 5 ** 2))
    print("Perimeter is {}cm.".format(2 * math.pi * 5))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()