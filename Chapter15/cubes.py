#Russell Arlt

import matplotlib.pyplot as plt


#Hands on #1
cubed =[]
five = [1,2,3,4,5]
for x in five:
    cubed.append(x*x*x)
ax1 = plt.subplot(2,3,1)
ax1.plot(five,cubed,marker="*", ls="--", c="purple", lw='2.0') #Hands on #3
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()


#Hands on #2
raised = []
for x in five:
    raised.append(x*x)
ax2 = plt.subplot(2,3,2)
ax2.plot(five,raised, marker="_", ls=":", c="gray", lw='3.0') #Hands on #3
plt.title("Raised Numbers")
plt.ylabel("Values Raised")
plt.xlabel("Input Values")
plt.grid()



#Hands on #4
biquadrate =[]
five = [1,2,3,4,5]
for x in five:
    biquadrate.append(x*x*x*x)
ax3 = plt.subplot(2,3,3)
plt.style.use("fast")
ax3.plot(five,biquadrate)
plt.title("BIQUADRATED! Numbers")
plt.ylabel("Values Biquadrated")
plt.xlabel("Input Values")
plt.grid()

plt.suptitle("FUN! With NUMBERS!")
plt.show()