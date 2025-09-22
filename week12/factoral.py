class Recursion:

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Recursion.factorial(n - 1)
        
    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return Recursion.fibonacci(n - 1) + Recursion.fibonacci(n - 2)
    #------------------End fibonacci------------------#

    def hanoi(n, from_rod, to_rod, aux_rod):
        print("------------------ This is Hanoi ------------------")
        if n == 1:
            print(f"ย้ายแผ่นดิส 1 จาก {from_rod} ไป {to_rod}")
            return
        
        Recursion.hanoi(n - 1, from_rod, aux_rod, to_rod)
        print(f"ย้ายแผ่นดิส {n} จาก {from_rod} ไป {to_rod}")
        Recursion.hanoi(n-1, aux_rod, to_rod, from_rod)
    #------------------End hanoi------------------#



display = Recursion
print("factorial is : 4! =", display.factorial(5))
print("------------------------------")

print("fibonacci  is : ")
for i in range(10):
    print(display.fibonacci(i), end=" ")


#hanoi
n = 3
display.hanoi(n, 'A', 'B', 'C')  # A, B and C are names of rods