#!/usr/bin/python3

def main():
    numArray = []


    while True:
        try: 
            value = input("Enter an index integer or type \"end\" to exit: ")
            if value == "end":
                break
            else:
                toIndexNumArray = int(value)
                numArray.append(toIndexNumArray)
        except ValueError:
            print("Please enter an integer instead.")
        except KeyboardInterrupt:
            print("\nExiting Program.")
            exit()
        except EOFError: 
            print("\nCaught an End of File Signal, Breaking out of Loop and Exiting")
            break

    return numArray

if __name__ == "__main__":
    result = main()
    print("The final list is: " + str(result))
    print("The sum of all integers is: " + str(sum(result)))
