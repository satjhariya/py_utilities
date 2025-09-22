def loop1():
    print("Inside loop 1")

def loop2():
    print("Inside loop 2")

def test_func(x:list):
    if not x:
        return
    loop_it = x.pop(0)
    for it in loop_it["it"]:
        loop_it["it_func"]()
        test_func(x.copy())

if __name__ == "__main__":
    a = [{"it":range(2),"it_func":loop1}, {"it":range(5,10),"it_func":loop2}]
    test_func(a)