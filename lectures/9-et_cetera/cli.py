import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")  # constructor for class ArgumentParser, description in -h/--help
parser.add_argument("-n", default=1, help="Number of times to meow", type=int)  # add "-n" to the parser & its description in -h/--help, default is 1 and expects int
args = parser.parse_args()  # parse the command line arguments

for _ in range(args.n):
    print("meow")