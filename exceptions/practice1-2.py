#!/usr/bin/python3

def main():
    numArray = [2,10,33,55,77,88,91,92,93,94,95]

    while True:
        try: 
            value = input("Enter an index integer or type \"end\" to exit: ")
            if value == "end":
                break
            else:
                toIndexNumArray = int(value)
                if toIndexNumArray < 0:
                    raise IndexError
                return numArray[toIndexNumArray]
        except ValueError:
            print("Please enter an integer instead.")
        except IndexError: 
            print("Please try a number between 0 and 9")


if __name__ == "__main__":
    result = main()
    print(result)
