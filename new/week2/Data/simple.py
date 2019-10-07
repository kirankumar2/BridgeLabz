class stack:
    def __init__(self):
        self.top = 0
        self.item = []

    def input_fun(self, data):
        for i in range(len(data)):
            if data[i] == "(":
                self.push(data[i])
            elif data[i] == ")":
                self.pop(data[i])
        self.disp()

    def push(self, ch):
        self.item.append(ch)
        self.top += 1

    def pop(self, da):
        if self.top <= 0:
            print ("False")
            exit(0)
        else:
            self.item.pop()
            self.top -= 1

    def disp(self):
        if self.top <= 0:
            print ("True")


if __name__ == "__main__":
    st = stack()
    expr = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"
    st.input_fun(expr)
