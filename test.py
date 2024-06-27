with open('test.txt','w') as file:
    file.write("elijah")
    
    file.write("xxxxxxx")
rd=open('test.txt','r')
for i in rd.readlines():
    for x1 in range(14):
        x=[]
        if x1<=10:
            print('adding...')
            name=True
            while name:
                print('[Info ::.stop iter]')
                name=False
                
                print('[Info ::.>>>>]')
                if x1==10:
                    name=False
                else:
                    print("[TRue...]")

            
            
        else:
            print("error")
            try:
                x[x1]
            except IndexError as error:
                print('index overlap error..')
        
        print(x)