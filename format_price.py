import argparse
import sys


def format_price(price):
    try:
        float_price = float(price)
    except (ValueError, TypeError):
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
