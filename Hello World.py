import time
import random
def animation_letter(tab1,tab2):
    tab3=[0]
    w=""
    for i in range(len(tab2)):
        for matrice in range(len(tab1)):
            print(w,tab1[random.randint(0,len(tab1)-1)],sep="")
            time.sleep(0.01)
        if tab3[0]==0:
            tab3[0]=tab2[i]
        else:
            tab3+=[tab2[i]]
        w+=tab2[i]
    return w

w=str(input("Write some word to animate : "))
tab1=["x","y","z","0","8","x","o","p","v","m","5","q","%","!","#","@","+"]
tab2 = [0]*len(w)
for composed in range(len(w)):
    tab2[composed]=w[composed]

print(animation_letter(tab1,tab2))

