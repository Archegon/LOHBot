import re

read = 'A B~ C/// D *E'
read = re.sub(r"[^a-zA-Z0-9 ]+", '', read)

print(read)