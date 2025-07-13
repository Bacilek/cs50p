def main():
    expr = input("Expression: ")
    x, y, z = expr.split(' ')

    x, z = int(x), int(z)
    match y:
        case '+':
            print(float(x + z))
        case '-':
            print(float(x - z))
        case '*':
            print(float(x * z))
        case '/':
            print(float(x / z))


main()
