import argparse
import sys
from decimal import Decimal, InvalidOperation


def format_whole_part(whole_part):
    return "{:,}".format(whole_part).replace(",", " ")


def format_fractional_part(fractional_part):
    fractional_part_normalized = abs(fractional_part.normalize())
    dot_index = 1
    return str(fractional_part_normalized)[dot_index:]


def is_whole_number(number):
    return number % 1 == 0


def is_valid_price_input(price):
    try:
        Decimal(str(price))
    except InvalidOperation:
        return False
    return True


def format_price(price):
    if not is_valid_price_input(price):
        return None

    price_number = Decimal(str(price))
    if is_whole_number(price_number):
        formatted_price = format_whole_part(price_number.to_integral())
    else:
        divisor = 1
        whole, fraction = divmod(price_number, divisor)
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
    if formatted_price is not None:
        print(formatted_price)
    else:
        sys.exit("Invalid input")
