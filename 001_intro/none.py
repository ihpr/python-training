"""
Create None2 object-brother of None using None and type().
Compare id’s. Discuss, which OOP pattern it is.
"""

none_2_type = type("None", (), {})
None2 = none_2_type()


def main() -> None:
    print(id(None2), id(None))
    print(None2 is None)
    print(None2 == None)

    return None


if __name__ == "__main__":
    main()
