import argparse
import math
import re
import sys
from numbers import Number


def is_valid_price(price):
    if (
        not isinstance(price, Number) and not isinstance(price, str)
    ) or isinstance(price, bool):
        return False
    elif isinstance(price, str) and re.search(r"[^\d.+-]", price) is not None:
        return False
    elif isinstance(price, Number) and not math.isfinite(price):
        return False
    else:
        return True


def format_price(price):
    if not is_valid_price(price):
        return None

    try:
        float_price = float(price)
    except ValueError:
        return None

    if float_price == 0:
        return "0"

    return (
        "{:,.2f}".format(float_price).replace(",", " ").rstrip("0").rstrip(".")
    )


def get_price_from_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("price")
    arguments = parser.parse_args()
    return arguments.price


if __name__ == "__main__":
    price = get_price_from_arguments()
    formatted_price = format_price(price)
    if formatted_price is not None:
        print(formatted_price)
    else:
        sys.exit("Invalid input")
