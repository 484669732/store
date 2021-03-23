class Watercup:
    __Name = ""
    __Height = ""
    __Volume = ""
    __Color = ""
    __Material = ""
    __Liquid = ""


    def Name(self, N):
        print(self.__Name, "ming",N)

    def Height (self,H):
        print(self.__Name, "gao",H)

    def Volume(self, V):
        print(self.__Name, "rong"；,V)

    def Color(self,C):
        print(self.__Name, "yan",C)

    def Material(self, M):
        print(self.__Name, "cai",M)

    def Liquid(self, L):
        print(self.__Name, "cai",L)

    def showMe(self):
        print("", self.__Name, "高度", self.__Height, "容积", self.__Volume, "颜色", self.__Color, "材质",self.__Material,"液体",self.__Liquid)

p = Watercup()
p.Name("水杯")
p.Height("5")
p.Volume("60")
p.Color("黑")
p.Material("塑料")
p.Liquid("水")
p.showMe()
