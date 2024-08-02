#----------Pi Calculation----------
import random
k= [1,10,100,1000,10000,100000,1000000]
z=0
for w in range(len(k)):
    for i in range(k[w]):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            z += 1
    print((4*z)/k[w])
    z=0
# you can change amount of "k" and see convergence


#----------Mensch Game----------
import random

jr = 0
jy = 0
jg = 0
jb = 0
exit_reason = None
p=[]
for i in range(10):
    jr = 0
    jy = 0
    jg = 0
    jb = 0
    exit_reason = None
    
    while jr < 44 and jy < 44 and jg < 44 and jb < 44:
        a = random.randint(1, 6)
        jr += a
        b = random.randint(1, 6)
        jy += b
        c = random.randint(1, 6)
        jg += c
        d = random.randint(1, 6)
        jb += d
    
        if jr >= 44:
            exit_reason = "jr"
        elif jy >= 44:
            exit_reason = "jy"
        elif jg >= 44:
            exit_reason = "jg"
        elif jb >= 44:
            exit_reason = "jb"
    
    p.append(exit_reason)

print("ehtemale borde red: ",int(p.count('jr'))/int(len(p)))
print("ehtemale borde yellow: ",int(p.count('jy'))/int(len(p)))
print("ehtemale borde green: ",int(p.count('jg'))/int(len(p)))
print("ehtemale borde bluee: ",int(p.count('jb'))/int(len(p)))
# you can run program multiple time and see answer
