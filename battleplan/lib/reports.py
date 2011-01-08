import re

String=0
Hash=1
Map=2

loc_p = re.compile('@([a-zA-Z0-9\-]+)')
hash_p = re.compile('#([a-zA-Z0-9]+)')

def tokenizer(str, pattern):
    while len(str) > 0:
        m = pattern.search(str)

        if m:
            b, e = m.span()
            if b != e: yield(False,str[:b])
            yield(True,m.group(1))
            str = str[e:]
        else:
            yield(False,str)
            break

def tokenize_report(s):
    for t1,p1 in tokenizer(s, hash_p):
        if t1:
            yield(Hash, p1)
            continue

        for t2,p2 in tokenizer(p1, loc_p):
            if t2:
                yield(Map, p2)
                continue
            yield(String, p2)
