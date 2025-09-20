class loop_cntrl:
    def __init__(self,it1=None,it2=None,it3=None,it4=None):
        self.it1 = it1
        self.it2 = it2
        self.it3 = it3
        self.it4 = it4
        
        #shared variables 
        self.i = None
        self.j = None
        self.k = None
    
    def loop4(self):
        if self.it4 is None:
            print("loop 4 is skipped no iterator 4")
            return
        for l in self.it4:
            print(f"Loop 4 i = {self.i}, j = {self.j}, k = {self.k}, l = {l}")

    def loop3(self):
        if self.it3 is None:
            print("loop 3 is skipped no iterator 3")
            return
        for k in self.it3:
            self.k = k
            print(f"Loop 3 i = {self.i}, j = {self.j}, k = {self.k}")
            self.loop4()


    def loop2(self):
        if self.it2 is None:
            print("loop 2 is skipped no iterator 2")
            return
        for j in self.it2:
            self.j = j
            print(f"Loop 2 i = {self.i}, j = {self.j}")
            self.loop3()


    def loop1(self):
        if self.it1 is None:
            print("loop 1 is skipped no iterator 1")
            return
        for i in self.it1:
            self.i = i
            print(f"Loop 1 i = {self.i}")
            self.loop2()

    def run(self):
        if self.it1 is not None and self.i is None:
            self.loop1()
        elif self.it2 is not None and self.j is None:
            self.loop2()
        elif self.it3 is not None and self.k is None:
            self.loop3()
        elif self.it4 is not None:
            self.loop4()
        else:
            print("Nothing to loop")
if __name__ == "__main__":

    p1 = loop_cntrl(range(1),range(2),range(3),range(4))
    p1.run()
    print(f"\n\n")
    p2 = loop_cntrl(None,None,range(3),range(4))
    p2.run()
    print(f"\n\n")

    p3 = loop_cntrl(None,None,None,range(4))
    p3.run()
    print(f"\n\n")

    p4 = loop_cntrl(None,range(2),None,range(4))
    p4.run()