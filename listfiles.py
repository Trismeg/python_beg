from os import walk
import hashlib

f = []
for (dirpath, dirnames, filenames) in walk("./"):
    f.extend(filenames)
    break

print f

thing = open("hashfile.txt", "w")

for i in range(len(f)):
    hasher = hashlib.sha256()
    with open(f[i], 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(hasher.hexdigest())
    thing.write(hasher.hexdigest()+"\n")

thing.close()

hasher = hashlib.sha256()
with open("hashfile.txt", 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print(" the final hash is ")
print(hasher.hexdigest())
