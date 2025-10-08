class recurse_loop:
        def __init__(self):
                self.result = {}
                self.data = {}
                self.num = 0
        def loop1(self,num=None):
                print(f"Inside loop 1 {num}")

        def loop2(self,num=None):
                print(f"Inside loop 2 {num}")

        def loop3(self,num=None):
                print(f"Inside loop 3 {num}")

        def loop4(self,num=None):
                print(f"Inside loop 4 {num}")

        def run(self, loop_list:list):
                if not loop_list:
                    return
                loop_it = loop_list[0]
                for it_n in loop_it["it"]:
                    loop_it["it_func"](it_n)
                    key = f"{loop_it['it_name']}_{it_n}"
                    if len(loop_list) == 1:
                        # Last level, store a value (could be anything, here just the value itself)
                        self.data.setdefault(key, [])
                        self.data[key].append(it_n)
                    else:
                        # Not last level, recurse and store nested dict
                        if key not in self.data:
                            self.data[key] = {}
                        # Save current data reference
                        prev_data = self.data
                        self.data = self.data[key]
                        self.run(loop_list[1:])
                        # Restore data reference
                        self.data = prev_data
                return self.data
import pandas as pd
if __name__ == "__main__":
        # loop_list = [
        #         {"it": range(2), "it_func": recurse_loop.loop1, "it_name": "i"},
        #         {"it": range(5, 10), "it_func": recurse_loop.loop2, "it_name": "j"},
        #         {"it": range(2), "it_func": recurse_loop.loop3, "it_name": "k"},
        #         {"it": range(2), "it_func": recurse_loop.loop4, "it_name": "l"}
        # ]

        loop_list = [
                {"it": range(2), "it_func": recurse_loop.loop1, "it_name": "i"},
                {"it": range(5, 7), "it_func": recurse_loop.loop2, "it_name": "j"}
        ]

        r = recurse_loop()
        print(r.run(loop_list))
        print(pd.DataFrame(r.data))
        