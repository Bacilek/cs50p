class Cat:
    MEOWS = 3  # "magic number" eliminated by a constant
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


def main():
    cat = Cat()
    cat.meow()


if __name__ == "__main__":
    main()