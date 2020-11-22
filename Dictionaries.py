
# stores data in key/value pairs (like a javascript object?)
# dictionary to convey a three digit month name to a full name

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# access by key
print(monthConversions["Mar"])

# access by get, with key
print(monthConversions.get("Dec"))

# when get fails, you will get 'none' so use a
# default value like so
print(monthConversions.get("Luv", "Not valid"))


