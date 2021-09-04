file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

file_counts["txt"]

"jpg" in file_counts
# dictionaries are mutable
file_counts["cgf"] = 8

print(file_counts)

del file_counts["cgf"]
print(file_counts)
