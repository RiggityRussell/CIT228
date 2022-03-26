import json
from matplotlib import pyplot as plt

filename = 'vizualization_project/data/readable_comet_data.json'
with open(filename) as f:
    comet_data = json.load(f)

comets = comet_data['meta']['view']['columns']

num_list = [*range(8,25)]

name_list = []
width_list = []

for num in num_list:
    comets1 = comets[num]
    comets2 = comets1.items()
    for key, value in comets2:
        if key == 'name':
            names = value
            name_list.append(names)
        if key =='width':
            width = value
            width_list.append(width)

iter = (len(name_list))
x = 0
while x < iter:
    print(f"The Comet name: {name_list[x]}, the width: {width_list[x]}")
    x += 1

fig, ax = plt.subplots()
ax.plot(name_list, width_list,marker='D', lw='1.0')
# plt.plot(width_list)
# plt.plot_date(name_list, width_list)
fig.autofmt_xdate()
plt.title("Width of Comets approaching close to Earth")
plt.ylabel("Width")
plt.xlabel("Name of COMET")
plt.show()