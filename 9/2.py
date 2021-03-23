class NotebookComputer:
    __name = ""
    __screen = ""
    __price = ""
    __cpu = ""
    __memory = ""
    __time = ""

    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setscreen(self,screen):
        self.__screen = screen
    def getscreen(self):
        return self.__screen
    def setprice(self,price):
        self.__price = price
    def getprice(self):
        return self.__price
    def setcpu(self,cpu):
        self.__cpu = cpu
    def getcpu(self):
        return self.__cpu
    def setmemory(self,memory):
        self.__memory = memory
    def getmemory(self):
        return self.__memory
    def settime(self,time):
        self.__time = time
    def gettime(self):
        return self.__time


    def typing(self,dazi):
        print(self.__name,"可以",dazi)
    def game(self,youxi):
        print(self.__name,"可以",youxi)
    def movie(self,dianying):
        print(self.__name,"可以",dianying)

dn = NotebookComputer()

dn.setname("笔记本电脑")
dn.setscreen("16寸")
dn.setprice(10000)
dn.setcpu("i7")
dn.setmemory("16GB")
dn.settime("10小时")

print(dn.getname(),"屏幕大小：",dn.getscreen(),"价格：",dn.getprice(),"CPU型号：",dn.getcpu(),"内存大小：",dn.getmemory(),"待机时长：",dn.gettime())
dn.typing("打字")
dn.game("玩游戏")
dn.movie("看电影")