"""Program that uses creates trigram text."""


import os


def main(src, num):
    """Main function."""
    tridict = parse_into_dict(src)
    return gen_text(tridict, num)
