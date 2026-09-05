# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Argparse Test Cases
#  Author       : Team Tinitiate
# ==============================================================================

import argparse
import sys


# Class to handle Custom Error Message in case an invalid argument is passed
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        print("")
        self.print_help()
        sys.exit(2)


# Function to handle the arguments and their values
def a(a=None, b=None, c=False, **kwargs):
    if a is not None:
        print("a", a)
    elif b is not None:
        print("b", b)
    elif c:
        print("c is selected")


# Function Main
if __name__ == "__main__":

    parser = MyParser()
    parser.set_defaults(method=a)

    # Arguments
    parser.add_argument(
        "-a",
        help="this is -a switch",
        type=int
    )

    parser.add_argument(
        "-b",
        help="this is -b switch",
        type=int
    )

    parser.add_argument(
        "-c",
        help="-c switch without parameters",
        action="store_true"
    )

    args = parser.parse_args()

    args.method(**vars(args))