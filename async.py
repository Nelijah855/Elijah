import asyncio

from threading import Thread

def first():
    print("first")
def second():
    print("second")
class x(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.th()

    def th(self):
        print("thread...")
        
        self.setDaemon(True)
        while True:
            print("[Info...].compiling-->xmc.h")
            print("[Info...].assembling-->xmc.o")
            print("[Info...].linking-->xmc.o")
            print("[Info...].packeged-->xmc.apkprint")

x=x()


async def elijah(delay):
    print("async....")

