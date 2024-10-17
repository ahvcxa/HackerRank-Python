
thickness = int(input())
c = 'H'


for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

for i in range(thickness+1):
    print(' '.ljust(thickness//2) + (c * thickness).center(thickness) + '  '.ljust(thickness * 3) + (c * thickness).rjust(
        thickness))

for i in range(thickness//2+1):
    print(' '.ljust(thickness//2) + ((c * thickness).center(thickness)) * 5)

for i in range(thickness+1):
    print(' '.ljust(thickness//2) + (c * thickness).center(thickness) + '  '.ljust(thickness * 3) + (c * thickness).rjust(
        thickness))

for i in range(thickness):
    print(
        ' '.rjust(thickness * 4) + (c * (thickness - i - 1)).rjust(thickness - 1) + c + (c * (thickness - i - 1)).ljust(
            thickness - 1))

