# Define var formatter to contain 4 {} strings
formatter = "{}, {}, {}, {}"
# Print and format var formatter to show 1234
print(formatter.format(1, 2, 3, 4))
# Print and format var formatter to show one two three four
print(formatter.format("one", "two", "three", "four"))
# Print and format var formatter to show True/False
print(formatter.format(True, False, False, True))
# Print and format var formatter to display string in var formatter
print(formatter.format(formatter, formatter, formatter, formatter))
# Print poem on new lines
print(formatter.format(
    "Try your",
    "\nOwn text here",
    "\nMaybe a poem",
    "\nOr a song about fear"
))
