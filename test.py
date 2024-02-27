import random, time




def program():
     
    n=5
    while n>0:

        x = ["+", "-", "*", "/"]
        symbol = random.choice(x)
        number1 = random.choice(range(1, 11))
        number2 = random.choice(range(1, 11))
        Time = time.time()
        print(f"{number1} {symbol} {number2}")
        answer=int(input("answer:>"))
        Time2 = time.time()
        based = Time2 - Time

        def remove_inx(input_value, index_to_keep):
            

            input_value_str = str(input_value)
            result = "".join([input_value_str[i]
                              for i in range(len(input_value_str)) if i in index_to_keep])
            return float(result)

        result = remove_inx(based, [0, 1])

        if symbol == "+":
            b= number1 + number2
        elif symbol == "-":
            b= number1 - number2
        elif symbol == "*":
            b= number1 * number2
        else:
            b= number1 / number2
        print(b)
        if b == answer and result<5:
            print("great!your answer is correct")

        elif b==answer and result>5:
            print("the answer is correct,but it took longer than the allotted time!")
        else:
            n -= 1
            print(f"your answer is incorrect!remaining chances:{n}")

program()




