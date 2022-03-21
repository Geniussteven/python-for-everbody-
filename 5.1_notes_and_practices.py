#5.1 notes
repeating steps 用while
So that was like a residual value of this little variable n after the last iteration（迭代） through the loop.
And that's because it was 1 and then we subtracted（减） 1 from it. And that got us to 0.
无限循环infinite loop

while True:
        line = input('> ')
        if line[0] == '#':
            continue
        if line =='done':
            break
        print(line)
print('Done!')
#definite loop定循环
#integer iteration variabies
#synax
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')
#5.3 loop idioms
