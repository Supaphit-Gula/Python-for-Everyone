
tilecolor={'red':100,'gold':200,'white':90,'grey':30}

print('----------------Tile Price------------------')
for c,t in tilecolor.items():
    print('color: {}  price:{}'.format(c,t))

print('----------------Program by user input V.2----------------')
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


buy_more=row-remain_tiles

print(f'Total tiles:{tiles} tiles')
print(f'one row finns {row} tiles')
print('Calculate')
print('Must have {} rows'.format(total_row))
print('There are remainings tiles that didnt use {} tiles'.format(remain_tiles))
print('Client must buy extra {} tiles'.format(buy_more))

print('-----------------The End------------------')


