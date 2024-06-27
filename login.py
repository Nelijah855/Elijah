




 


password=open('password.txt','r')


class Login():
    def __init__(self):
        self.read_write('2013','cede')
        self.file_check() 
    def read_write(self,password1,name1):
        password=open('password.txt','w')
        password.write(password1)
        nam=open('name.txt','w')
        print('working...............')
        nam.write(name1)
        
    
    def file_check(self):
        
        if self.is_name()==True or self.is_password==True:
            print('true......')
            return True
        else:
            print('false....')
            return False

    
        
    def file_write(self):
        pass
    def file_read(self):
        pass

    def is_name(self):
        nam=open('name.txt','r')
        

        x=nam.read()
        print("this is x name value",x)
        if x==None:
            print('false name...........')
            return False
            
        else:
            print('true name...........')
            
            return True
    

    def is_password(self):
        x=password.read()
        print("this is x password value",x)
        if x==None:
            print("false password......")

            
            return False
        
        else:
            print('true password....')
        
            return True
l=Login()
l.is_password()