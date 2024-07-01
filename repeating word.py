s = 'abssrcdebabsaffgfc'
x = 'a'
y = 'c'

for i in range(len(s)):
    if s[i] == x:
        for j in range(i, len(s)):

            if s[j] == y:
                print(s[i:j + 1])