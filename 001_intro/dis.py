"""
Write simple function, for example sum of 2 arguments or calling len() 
on argument and explain bytecode for the function using ‘dis’ module.
"""


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print(add(1, 2))


if __name__ == "__main__":
    main()    
