from loop_functions import func_map
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

        self.result = {}

    def loop4(self,i=None,j=None,k=None):
        if self.it4 is None:
            print("loop 4 is skipped no iterator 4")
            return
        for l in self.it4:
            arg_map = {
                "a": {"x": 10 + l},
                "b": {"x": 20 + l, "y": 30 * l},
                "c": {"x": 10, "y": 20, "z": 30},
                "d": {}
            }
            print(f"Loop 4 i = {i}, j = {j}, k = {k}, l = {l}")
            for key, func in func_map.items():
                func(**arg_map[key])
                print(arg_map[key])
            self.result[i][j][k][l] = i+j+k+l
            
            
    def loop3(self,i=None,j=None):
        if self.it3 is None:
            self.result[i][j][3] = {}
            print("loop 3 is skipped no iterator 3")
            return
        for k in self.it3:
            if k not in self.result[i][j]:
                self.result[i][j][k] = {}
            self.k = k
            print(f"Loop 3 i = {self.i}, j = {self.j}, k = {self.k}")
            self.loop4(i,j,k)

    def loop2(self, i=None):
        if self.it2 is None:
            self.result[i][2]= {}
            print("loop 2 is skipped no iterator 2")
            return
        for j in self.it2:
            if j not in self.result[i]:
                self.result[i][j] ={}
            print(f"Loop 2 i = {i}, j = {j}")
            self.loop3(i,j)

    def loop1(self):
        if self.it1 is None:
            print("loop 1 is skipped no iterator 1")
            self.result[1] = {}
            return
        for i in self.it1:
            if i not in self.result:
                self.result[i] = {}
            print(f"Loop 1 i = {i}")
            self.loop2(i)

    def run(self):
        if self.it1 is not None and self.i is None:
            self.loop1()
        elif self.it2 is not None and self.j is None:
            # Provide a default or explicit i value here
            for i in range(1):  # or any default range you want
                self.result[i] = {}
                self.loop2(i)
        elif self.it3 is not None and self.k is None:
            # Similarly, provide i and j
            for i in range(1):
                for j in range(1):
                    self.result[i] = {}
                    self.result[i][j] = {}
                    self.loop3(i, j)
        elif self.it4 is not None:
            # Provide i, j, k
            for i in range(1):
                for j in range(1):
                    for k in range(1):
                        self.result[i] = {}
                        self.result[i][j] = {}
                        self.result[i][j][k] = {}
                        self.loop4(i, j, k)
        else:
            print("Nothing to loop")
if __name__ == "__main__":

    # p1 = loop_cntrl(range(1),range(2),range(3),range(4))
    # p1.run()
    # print(p1.result)
    # print(f"\n\n")

    p2 = loop_cntrl(None,None,
                    None,range(3))
    p2.run()
    print(p2.result)