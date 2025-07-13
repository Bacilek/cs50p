import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow(f"helo, {sys.argv[1]}")
