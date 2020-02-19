# def temperature(*args):
#     product = []
#     def celsius2fahrenheit(x):
#         return 9 * x / 5 + 32
    
#     for t in args:
#         result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
#         product.append(result)
    
#     return product

# print(temperature(5, 6, 105, 6, 10, 5, 6, 105, 6, 10, 5, 6, 105, 6, 10))



def temperature(**kwargs):
    product = []
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32
    

    for k, v in kwargs.items():
        result = "It's " + str(celsius2fahrenheit(v)) + " degrees!"
        product.append(result)
        print(f"{k}: {v}")


    return product

print(temperature(a=21, b=33, c=40, np=-100))