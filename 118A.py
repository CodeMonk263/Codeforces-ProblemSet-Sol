string = raw_input().lower()
notvowl = ".".join([c for c in string if not c in "aiueoy"])

print "." + notvowl
