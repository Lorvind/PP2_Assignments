global_var = 42

local_var = 8

def myFunction():
    local_var = 24
    print(local_var + global_var)

print(local_var + global_var)