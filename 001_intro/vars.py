"""
Create variables with code:
* a=XXX
* b=XXX
where XXX is:
* 1
* 65000
* ‘Hello’
* ‘#hashtag@’

Print id and refcount of a and b to console. Discuss results with mentor.
"""

import sys


def print_id_and_refcount(a, b) -> None:
    for val in (a, b):
        print(f"id: {id(val)}, refcount: {sys.getrefcount(val)}")

    return None


def main():
    a = 1
    b = 1

    print_id_and_refcount(a, b)

    a = 65000
    b = 65000

    print_id_and_refcount(a, b)

    a = "Hello"
    b = "Hello"

    print_id_and_refcount(a, b)

    a = "#hashtag@"
    b = "#hashtag@"

    print_id_and_refcount(a, b)


if __name__ == "__main__":
    main()
