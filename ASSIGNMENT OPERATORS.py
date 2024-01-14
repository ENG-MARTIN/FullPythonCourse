# ====================================    OPERATORS   ====================================================
# assignment operator
a=2
b=3 
c=a+b
print(c)

x=[1,2,3]
y=x
#----------- using the copy function
z=x.copy()

#------------ using the append function
x.append(4)

# --------- using the is operator ---
#  the is operator is used to test for object identity. It checks whether two variables reference the same object in memory
val1=3
val2=val1
val3=val2
print(val3 is val1)


result=(y==z, y is z)
print(result)
#=================================== getting the average =========================================

# using the input function
inputone= eval(input("Enter a your first nummber"+'\n'))
total=c+inputone
average=total/2
print(average)
 
 # ------Loops--------

my_set=['martin','racheal']
reversed_set=my_set.reverse
print(reversed_set)

b=[1,3,4,5,6]
for i in b:
    i=i+i
    print(i)

# =================================================Addition Assignment (+=):=============================
    x += 5  # Equivalent to: x = x + 5


# ================================================ Subtraction Assignment (-=):============================
    x -= 3  # Equivalent to: x = x - 3


# ================================================  Multiplication Assignment (*=): ========================
    x *= 2  # Equivalent to: x = x * 2


#  =============================================   Division Assignment (/=): ==========================
    x /= 4  # Equivalent to: x = x / 4

#  =Floor Division Assignment (//=): =======The //= operator performs floor division on the current value of the variable on the left side by the value on the right side and assigns the result to the variable.
x //= 3  # Equivalent to: x = x // 3

