def main():
    file = input("file: ").lower().strip()

    if '.' in file:
        filename, extension = file.rsplit('.', maxsplit=1)

        match extension:
            case "jpg":
                print("image/jpeg")
            case "gif" | "png" | "jpeg":
                print(f"image/{extension}")
            case "pdf" | "zip":
                print(f"application/{extension}")
            case "txt":
                print("text/plain")
            case _:
                print("application/octet-stream")
    else:
        print("application/octet-stream")

main()
