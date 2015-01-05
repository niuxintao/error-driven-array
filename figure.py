"""
This shows an example of the "fivethirtyeight" styling, which
tries to replicate the styles from FiveThirtyEight.com.
"""


from matplotlib import pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y1 = [1,1,1,0.582136741,0.865286844]
y2 = [0.171231318, 0.782517585,0.487110159,0.180418895,0.565121413]
y3 = [0.358207799,0.5767471,0.21759905,1,1]



fig = plt.figure()


line_1, = plt.plot(x, y1,  marker="s",  color="k")
line_2, = plt.plot(x, y2, ls="--", marker="d", mfc="None",   color="k")
line_3, = plt.plot(x, y3, ls="-.", marker="o", mfc="None",   color="k")

#configure legend
fig.legend([line_1, line_2, line_3], ['elda', 'fglt','ela'] )


#configure axis

#123
plt.ylim(0, 1.05)


plt.yticks(np.arange(0, 1.05, 0.1))

#hide Y tick labels for some plots(only plots on the left and right have labels and ticklabels
##ax2.set_yticklabels([]) 
##ax3.set_yticklabels([])

plt.xlim(1, 5)

plt.xticks(np.arange(1, 6, 1))

ax = plt.subplot()
ax.set_xticklabels([ 'Tomcat','Hsql','Gcc','JFlex', 'Tcas'])


#plt.yaxis.tick_left()

#plt.xlabel(r"$SUT$")

plt.ylabel(r"$f-measure\ /\ tests$")

plt.subplots_adjust(left=0.10, bottom=0.11, right=0.84, top=0.98, wspace=0.25, hspace=0.25);


plt.show()
