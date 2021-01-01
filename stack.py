from array import *
stack = array('i', [])
top = -1
n = int(input("Enter the size of the stack: "))
while True:
    a = int(input("\nEnter 1.Push 2.Pop 3.Display 4.Top Element 5.Stop:\n"))
    if a == 1:
        if top >= n-1:
            print("\nOverflow condition!!!\n")
        else:
            b = int(input("Enter the element to push:\n"))
            stack.append(b)
            top = top+1
    elif a == 2:
        if top <= -1:
            print("\nUnderflow condition!!!\n")
        else:
            y = stack[top]
            print("\nThe popped elements is", y)
            stack.pop(top)
            top = top-1
    elif a == 3:
        if top <= -1:
            print("\nUnderflow condition!!!\n")
        else:
            print("\nThe elements in the stack are")
            i = top
            while i >= 0:
                print(stack[i])
                i -= 1
    elif a == 4:
        if top <= -1:
            print("\nUnderflow condition!!!\n")
        else:
            z = stack[top]
            print("The top element is", z)
    elif a == 5:
        break
    else:
        print("\nInvalid entry!!!\n")
print(type(stack))
