# Data structures

# list  =   sequence of mutable values
# tuple =   sequence of immutable values
# set   =   collection of unique values
# dict  =   collection of key-value pairs

# Create an empty set
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(2)
s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")