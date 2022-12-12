import matplotlib.pyplot as plt


#'.pie' function creates the pie chart
#Creating the legend for the pie chart (Make sure to add labels to .pie)
sizes = [50,23,7,15,5]
labels = ['Green','Yellow','Purple','Red','Blue']
plt.pie(sizes)
plt.axis('equal')


#Changing the angle of the chart and color
colors = ['green','yellow','purple','red','blue']
plt.pie(sizes,colors=colors,startangle=90,labels=labels)
plt.title("Pie chart example")


#Location [loc] of the legend can be changed
plt.legend(title="Legend",loc='upper left')

#supported values are 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'

plt.show()

