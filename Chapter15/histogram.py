import matplotlib.pyplot as plt
#scores showing how many yards students ran in 12 minutes
# 1 mile = 1,760 yards
fitness_test=[2901,1760,3000,2824,3235,2050,2265,2500,2400,2625,3550,1850,1890,3200,2900,2975,3000,2220,2250]
plt.hist(fitness_test, bins=9, color="purple")
plt.ylabel("Number of Students")
plt.xlabel("Yards ran in 12 minutes")
plt.suptitle("Scores showing how many yards students ran in 12 minutes")
plt.show()


# fitSort = sorted(fitness_test)
# print(fitSort)
