


def read_write(password,name):
    password=open('password.txt','w')
    password.write(str(password))
    nam=open('name.txt','w')
    nam.write(name)

    

nam=open('name.txt','w')

password=open('password.txt','r')


class Login():
    def __init__(self):
        
        pass
    def file_check(self,x,y):
        password=open('password.txt','w')
        password.write(str(x))
        nam=open('name.txt','w')
        nam.write(y)
    def file_write(self):
        pass
    def file_read(self):
        pass

    def is_name(self):
        nam=open('name.txt','r')
        if nam.readlines()!=None:
            return True
        else:
            
            return False
    

    def is_password(self):
        if password.readlines()!=None:

            
            return True
        else:
        
            return False
l=Login('elijah','comjj')
print(l.is_name())
print(l.is_password())