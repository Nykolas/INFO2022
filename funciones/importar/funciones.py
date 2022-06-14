

def primo(number):
    if number < 2:
        return False
    for n in range(2, number):
        if number%n == 0:
            return False

    return True



if __name__ == '__main__':
	print("HOLA")

