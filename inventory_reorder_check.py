inventory = {"Brush":120,"Roller":200,"Hammer":50 ,"Nails":100 ,"Paint":30,"Screwdriver":45 , "Wire":109}

count=0
for key,value in inventory.items():
    if value<70:
        print(f'{key} : REORDER NEEDED : CURRENT STOCK : {value}')
        count+=1
    else:
        print(f'{key} : STOCK OK : CURRENT STOCK : {value}')
print(f'{count} ITEMS NEED TO BE REORDER')
    
print(inventory)
