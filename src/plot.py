import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def drawPlot(points, pt1, pt2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    setColor = ['black', 'red', 'blue', 'orange', 'darkorchid', 'green']
    for i in range(len(pt1)):
        for point in points:
            x, y, z = point
            if point == pt1[i] or point == pt2[i]:
                ax.plot([x], [y], [z], marker='o',
                        markersize=4, color=setColor[i % 6])
            else:
                ax.plot([x], [y], [z], marker='o',
                        markersize=4, color='silver')

    # Set the labels for the x, y, and z axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()
