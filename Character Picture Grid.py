# Below is given List of lists. the code turns the given grid like this [Question is taken from Automate Boring Stuff with Python book]
#  ..OO.OO..
#  .OOOOOOO. 
#  .OOOOOOO. 
#  ..OOOOO.. 
#  ...OOO... 
#  ....O....
#------------------------------------------------------------------------
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
str=""
for i in range(0,6):
    for j in range(0,9):
        str = str + grid[j][i]
    print(str)
    str= ""
