import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def drawPlotResult(minPoint1,minPoint2):
    setColor = ['red', 'blue', 'orange',
                'darkorchid', 'green', 'black', 'yellow']
    for i in range(len(minPoint1)):
        x, y, z = minPoint1[i]
        ax.plot([x], [y], [z], marker='o',markersize=7, color=setColor[i % 6])
        x,y,z = minPoint2[i]
        ax.plot([x], [y], [z], marker='o',markersize=7, color=setColor[i % 6])

def drawPlot(points,minPoint1,minPoint2):
    for point in points:
        if(point not in minPoint1) and (point not in minPoint2): 
            x, y, z = point
            ax.plot([x], [y], [z], marker='o',markersize=5, color='darkgrey')

    # Set the labels for the x, y, and z axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()