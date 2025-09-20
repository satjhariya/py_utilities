class op_funs:
    def __init__(self):
        pass
    @staticmethod
    def func_a(x):
        print(f"funcition a is called with {x}")
    
    @staticmethod
    def func_b(x,y):
        print(f"funciton b is called with parameters {x} and {y} \n\t\
               the result is {x+y}")

    @staticmethod
    def func_c(x,y,z):
        print(f"function c is called \
              with params {x}, {y} and {z}\n\t\
              the result is {x*y*z}")
    
    @staticmethod
    def func_d():
        print(f"funciton d is called")

func_map = {
    "a" : op_funs.func_a,
    "b" : op_funs.func_b,
    "c" : op_funs.func_c,
    "d" : op_funs.func_d
}
