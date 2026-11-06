import sys

a = 1
b = 65000
c = "Hello"
d = "#hastag@"

print(
    f"id(a): {id(a)} refcount: {sys.getrefcount(a)} "
    f"id(b): {id(b)} refcount: {sys.getrefcount(b)} "
    f"id(c): {id(c)} refcount: {sys.getrefcount(c)} "
    f"id(d): {id(d)} refcount: {sys.getrefcount(d)}"
)
