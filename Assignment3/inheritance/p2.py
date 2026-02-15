class qqw2z:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def output(self):
        return self.var1

class Something(qqw2z):
    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2)
        self.var3 = var3

    
instance = Something(1, 2, 3)

print(instance.var3)