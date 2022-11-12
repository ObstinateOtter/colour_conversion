def rgb_to_hex():
    R = int(input("Value of Red: "))
    G = int(input("Value of Green: "))
    B = int(input("Value of Blue: "))
    HEX = '#'+str(hex(R))+str(hex(G))+str(hex(B))
    print("\n \nHex value conversion is:", HEX.replace('0x',''))

def hex_to_rgb():
    hex = input("Enter the Hex code: ")
    lst = list(hex.replace('#',''))
    R = int(lst[0]+lst[1],16)
    G = int(lst[2]+lst[3],16)
    B = int(lst[4]+lst[5],16)
    print('The Value of Red:',R)
    print('The Value of Green:',G)
    print('The Value of Blue:',B)
    
while True:
    ch = int(input("1.RGB to HEX conversion \n2.HEX to RGB conversion \n3.Exit \nEnter Choice: "))
    if ch == 1:
        rgb_to_hex()
    elif ch == 2:
        hex_to_rgb()
    elif ch == 3:
        exit()
    else:
        print('Invalid Input!!!')
