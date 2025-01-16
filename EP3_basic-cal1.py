
tilecolor={'red':100,'gold':200,'white':90}

print('Program by user input')
try:
    tiles=int(input('How many total tiles do you want to use:'))
    row=int(input('How many tiles using for 1 row:'))
    color=input('What the color of tiles[red/gold/white]:')
except:
    print('Please input in number only!!')
    tiles=int(input('How many total tiles do you want to use:'))
    row=int(input('How many tiles using for 1 row:'))
    color=input('What the color of tiles[red/gold/white]:')

print('------------------Calculate------------')
total_row=tiles//row
remain_tiles=tiles%row
#print(total_row,remain_tiles)

buy_more=row-remain_tiles

print(f'Total tiles:{tiles} tiles')
print(f'one row finns {row} tiles')
print('Calculate')
print('Must have {} rows'.format(total_row))
print('There are remainings tiles that didnt use {} tiles'.format(remain_tiles))
print('Client must buy extra {} tiles'.format(buy_more))



