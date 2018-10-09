import argparse
import sys
from decimal import Decimal, InvalidOperation


def is_valid_price_input(price):
    try:
        Decimal(str(price))
    except InvalidOperation:
        return False
    return True


def format_price(price):
    if not is_valid_price_input(price):
        return None

    float_price = float(price)
    return (
        "{:,.2f}".format(float_price).replace(",", " ").rstrip("0").rstrip(".")
    )


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
