def AtomicDictionary():
    d={"fe":"iron","p":"phosphorus","n":"nitrogen"}
    print(d)

    symbol=input("enter the symbol\n")
    element=input("enter the element\n")

    if symbol in d.keys():
            print("key exists and hence value is replaced")
    else:
            print("new key and value added to dictionary")
    d[symbol]=element
    print(d)

    print("length of dictionary: ",str(len(d)))

    key=input("enter the symbol to search\n")
    if key in d.keys():
        print(d[key])
    else:
        print("key does not exists in dictionary")

AtomicDictionary()
