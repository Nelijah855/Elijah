class Method():
    @staticmethod
    def static():
        print("staticmethod...")
        while True:
            print("[Info..linking]")
        return ""
    @classmethod
    def clas(self):
        print("@classmethod ...")
        while True:
            print("[Info..linker]")
    @property
    def pro(self):
        print(self.__dict__.values())
        print("@property...")
        return True
        

x=Method()
#x.static()
#x.clas()
x.pro