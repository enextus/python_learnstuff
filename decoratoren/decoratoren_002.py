def f(*args, **kwargs):
    
    for i in args:
        print(f"i: {i}")

    print("\n")
    for key, value in kwargs.items():
        print(f"The value of {key} is {value}")

    print("\n")

    def g():
        print("01. Hallo, ich bin es, 'g'")
        print("02. Danke für's Aufrufen")
        
    print("03. Dies ist die Funktion 'f'")
    print("04. 'f' ruft nun 'g' auf!")
    
    g()

f(2, 4, _1="Shark", _2=4.5, _3=True)