astring = "Hello world!"
astring2 = 'Hello world!'

print("Single quotes are ' '")
print("Length of astring is %d" % len(astring))
print("Index of o is %d" % astring.index("o"))
print("Count of l in %s is %d" % (astring, astring.count("l")))
print("Substring %s" % astring[3:7])
print("Uppercase ", astring.upper())
print("Uppercase ", astring.lower())
print("Startswith ", astring.startswith("Hello"))
print("Endswith ", astring.startswith("kjsdafakgfakf"))
print("String split", astring.split(" "))