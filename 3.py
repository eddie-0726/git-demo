
while True:
    try:   
        a_input = (input("請輸入a:"))
        if a_input== "exit":
            break
        a = eval(a_input)
        b = eval(input("請輸入b:"))

        if a == b :
            print("ab一樣大")
        elif a > b:
            print(f"a>b ,相差:{a-b}")
        else:
            print(f"b>a ,相差:{b-a}")

    except Exception as e :
        print(f"發生錯誤，{e}")

