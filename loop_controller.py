class loop_cntrl:
    def __init__(self,iterator1,iterator2):
        self.it1 = iterator1
        self.it2 = iterator2

    def loop_1(self):
        for it in self.it1:
            print(f"loop1_{it}")

    def loop_2(self):
        for it in self.it2:
            print(f"loop2_{it}")
            self.loop_1()

    def run(self):
        self.loop_2()
if __name__ == "__main__":
    loops = loop_cntrl(range(5),range(6))
    loops.run()
