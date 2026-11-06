None2Type = type("None", (), {})
None2 = None2Type()

print(id(None2), id(None))
print(None2 is None)
print(None2 == None)