Data = [('a', ['b', 'c']),
        ('e', ['f', 'g', 'a'])
        ]

x = 'e  '
if x in Data:
        print(f"{x} belongs to {Data}")
else:
        print(f"{x} does not belong to {Data}")

for elem in Data:
        if elem[0] == x:
                print(f"{x} belongs to {Data}")
                print(f"neighbours : {elem[1]}")
                break
