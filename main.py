import sys

def get_arg():
    argument = ""
    try:
        if (len(sys.argv) == 1):
            argument = sys.argv[1]
        if (len(sys.argv) > 1):
            for i in sys.argv:
                if (i != sys.argv[0]):
                    argument += (i + " ")
    except IndexError:
        print("Necessitamos de pelo menos um argumento para conseguir rodar")
    finally:
        return argument
pass

if __name__ == "__main__":
    argument = get_arg()
    if argument != "":
        print(f"O argumento a ser pesquisado é: {argument}")
    pass
pass
