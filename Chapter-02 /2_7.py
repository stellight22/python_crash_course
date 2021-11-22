#2-7 Stripping names
# store a person's name, nad include some whitespace at beg and end
#make sure to use \t and \n at least once

#print the name once, then print using lstrip, rstrip, strip

name = "  Los \tangeles\n  "
print("original version:" + name)

print("left strip:" + name.lstrip())
print("right strip: " +name.rstrip())
print("strip:" + name.strip())