import matplotlib.pyplot as plt


labels=["PNG", "JPEG", "SVG", "GIF", "OTHER"]
numUsed=[376, 348, 153, 104, 19]
explode=(0,.1,.2,.3,.4)
wedgeColors=('purple','grey','yellow','blue','green')

fig1, ax1= plt.subplots()
ax1.pie(numUsed, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=50, colors=wedgeColors)
ax1.axis('equal') #equal aspect ratio ensures that pie is drawn as a circle
plt.suptitle("Popular Graphic Formats on the Web")

plt.show()
