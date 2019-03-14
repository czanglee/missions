import itertools
import string
import hashlib
import re

p = re.compile("^0+[e]{1}[0-9]+$")
test = "0e12345678901234567890123456789012345678901234567890123456789012"
if p.match(test):
    print("Test match! ",test)

for char in list(range(15, 30)):
    for s in itertools.product(string.printable, repeat=char):
        s = ''.join(s)
        hash_object = hashlib.sha256(s.encode('utf-8')).hexdigest()
        if p.match(hash_object):
            print(s, ' - ', hash_object)





