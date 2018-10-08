import argparse
import sys
from decimal import Decimal, InvalidOperation


def format_whole_part(whole_part):
    return "{:,}".format(whole_part).replace(",", " ")


def format_fractional_part(fractional_part):
    fractional_part_normalized = abs(fractional_part.normalize())
    return str(fractional_part_normalized)[1:]


def is_whole_number(number):
    return number % 1 == 0


def format_price(price):
    try:
        number = Decimal(str(price))
    except InvalidOperation:
        # raise ValueError("Invalid price string")
        return None

    if is_whole_number(number):
        formatted_price = format_whole_part(number.to_integral())
    else:
        whole, fraction = divmod(number, 1)
        formatted_price = "{}{}".format(
            format_whole_part(whole), format_fractional_part(fraction)
        )
    return formatted_price


def load_price():
    parser = argparse.ArgumentParser()
    parser.add_argument("price")
    arguments = parser.parse_args()
    return arguments.price


if __name__ == "__main__":
    price = load_price()
    formatted_price = format_price(price)
    if formatted_price:
        print(formatted_price)
