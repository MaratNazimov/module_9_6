def all_variants(text):
    for x in range(1, len(text) + 1):
        for j in range(len(text) - x + 1):
            yield text[j: x + j]

a = all_variants("abc")
for i in a:
    print(i)
