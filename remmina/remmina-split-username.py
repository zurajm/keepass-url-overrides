#!/usr/bin/python
import sys
if len(sys.argv) < 2:
    quit()
# print(repr(sys.argv[1]))
words = str(sys.argv[1])
# print(words)
# words = r"user"
if "\\" in words:
    domain = words.split("\\")[0]
    user = words.split("\\")[1]
    print("domain={domain}\\n".format(domain=domain))
    print("username={user}".format(user=user))
else:
    print("username={words}".format(words=words))
