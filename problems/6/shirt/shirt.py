from sys import argv, exit

from PIL import Image, ImageOps

from os import path

EXTENSIONS = (".jpg", ".jpeg", ".png")  # tuple
SHIRT = "shirt.png"

def main():
    if len(argv) != 3:
        exit("Usage: python shirt.py input output.")

    infile, outfile = argv[1], argv[2]
    infile_extension = path.splitext(infile)
    outfile_extension = path.splitext(outfile)

    if infile_extension[1] != outfile_extension[1]:
        exit("Error: input files must match extensions.")

    if infile_extension[1] not in EXTENSIONS or \
        outfile_extension[1] not in EXTENSIONS:
        exit("Error: input files must end with '.jpg', '.jpeg' or '.png'.")

    try:
        with Image.open(infile) as muppet, Image.open(SHIRT) as shirt:

            muppet = ImageOps.fit(muppet, shirt.size) # resize & fit
            muppet.paste(shirt, shirt) # image.paste(coords, mask)
            muppet.save(outfile)

    except FileNotFoundError:
        exit(f"Error: {infile} or {SHIRT} not found.")



if __name__ == "__main__":
    main()
