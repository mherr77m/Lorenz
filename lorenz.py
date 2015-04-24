import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib.gridspec as gridspec 

def lorenz(x, y, z, s=10, r=28, b=2.667) :
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

dt = 0.01
stepCnt = 20000

# Need one more for the initial values
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))

# Setting initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Stepping through "time".
for i in range(stepCnt) :
    # Derivatives of the X, Y, Z state
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

x = []
y = []
z = []

for t in range(20):
    # Need one more for the initial values
    xs2 = np.empty((stepCnt + 1,))
    ys2 = np.empty((stepCnt + 1,))
    zs2 = np.empty((stepCnt + 1,))

    # Setting initial values
    mean = 0
    sdev = .5
    xs2[0], ys2[0], zs2[0] = (-15.7+random.normalvariate(mean, sdev), 
                              -6.5+random.normalvariate(mean, sdev), 
                              44.+random.normalvariate(mean, sdev))

    # Stepping through "time".
    for i in range(stepCnt) :
        # Derivatives of the X, Y, Z state
        x_dot, y_dot, z_dot = lorenz(xs2[i], ys2[i], zs2[i])
        xs2[i + 1] = xs2[i] + (x_dot * dt)
        ys2[i + 1] = ys2[i] + (y_dot * dt)
        zs2[i + 1] = zs2[i] + (z_dot * dt)

    x.append(xs2)
    y.append(ys2)
    z.append(zs2)

x2 = []
y2 = []
z2 = []

for t in range(20):
    # Need one more for the initial values
    xs2 = np.empty((stepCnt + 1,))
    ys2 = np.empty((stepCnt + 1,))
    zs2 = np.empty((stepCnt + 1,))

    # Setting initial values
    mean = 0
    sdev = .5
    xs2[0], ys2[0], zs2[0] = (.14+random.normalvariate(mean, sdev), 
                              .32+random.normalvariate(mean, sdev), 
                              13.6+random.normalvariate(mean, sdev))

    # Stepping through "time".
    for i in range(stepCnt) :
        # Derivatives of the X, Y, Z state
        x_dot, y_dot, z_dot = lorenz(xs2[i], ys2[i], zs2[i])
        xs2[i + 1] = xs2[i] + (x_dot * dt)
        ys2[i + 1] = ys2[i] + (y_dot * dt)
        zs2[i + 1] = zs2[i] + (z_dot * dt)

    x2.append(xs2)
    y2.append(ys2)
    z2.append(zs2)

x3 = []
y3 = []
z3 = []

for t in range(20):
    # Need one more for the initial values
    xs3 = np.empty((stepCnt + 1,))
    ys3 = np.empty((stepCnt + 1,))
    zs3 = np.empty((stepCnt + 1,))

    # Setting initial values
    mean = 0
    sdev = .5
    xs3[0], ys3[0], zs3[0] = (-9+random.normalvariate(mean, sdev), 
                              -4+random.normalvariate(mean, sdev), 
                              33+random.normalvariate(mean, sdev))

    # Stepping through "time".
    for i in range(stepCnt) :
        # Derivatives of the X, Y, Z state
        x_dot, y_dot, z_dot = lorenz(xs3[i], ys3[i], zs3[i])
        xs3[i + 1] = xs3[i] + (x_dot * dt)
        ys3[i + 1] = ys3[i] + (y_dot * dt)
        zs3[i + 1] = zs3[i] + (z_dot * dt)

    x3.append(xs3)
    y3.append(ys3)
    z3.append(zs3)

for i in range(1000):
    fig = plt.figure(figsize=(10,5))
    print i 
    gs2 = gridspec.GridSpec(3, 4)
    gs2.update(left=0.0, right=0.95, hspace=0.2)
    ax = plt.subplot(gs2[:, :-2],projection='3d')
    ax2 = plt.subplot(gs2[0, -2:])
    ax3 = plt.subplot(gs2[2, -2:])
    ax4 = plt.subplot(gs2[1, -2:])

    ax.set_title("Lorenz Attractor")
    ax.set_xlabel("X Axis",fontsize=8)
    ax.set_ylabel("Y Axis",fontsize=8)
    ax.set_zlabel("Z Axis",fontsize=8)
    ax.scatter(xs[:], ys[:], zs[:],'grey',s=1,edgecolor='none')
    for t in range(len(x)):
        if i < 300:
            ax.plot(x[t][:i], y[t][:i], z[t][:i],'g',linewidth=.5)
            ax.plot(x2[t][:i], y2[t][:i], z2[t][:i],'r',linewidth=.5)
            ax.plot(x3[t][:i], y3[t][:i], z3[t][:i],'m',linewidth=.5)
        else:
            ax.plot(x[t][i-299:i], y[t][i-299:i], z[t][i-299:i],'g',linewidth=.5)
            ax.plot(x2[t][i-299:i], y2[t][i-299:i], z2[t][i-299:i],'r',linewidth=.5)
            ax.plot(x3[t][i-299:i], y3[t][i-299:i], z3[t][i-299:i],'m',linewidth=.5)
    ax.set_xlim(-20,25)
    ax.set_ylim(-30,30)
    ax.set_zlim(0,60)

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(8)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(8)
    for tick in ax.zaxis.get_major_ticks():
        tick.label.set_fontsize(8)


    ax2.set_ylabel('x-position',fontsize=8)
    
    for t in range(len(x)):
        ax2.plot(range(i),x[t][:i],'g')
    ax2.set_ylim(-20,20)
    ax2.set_xticks(range(0, 20000, 50))
    if (i < 300):
        ax2.set_xlim(0,300)
    else:
        ax2.set_xlim(i-299,i+1)
    
    for tick in ax2.xaxis.get_major_ticks():
        tick.label.set_fontsize(8)
    for tick in ax2.yaxis.get_major_ticks():
        tick.label.set_fontsize(8)

    ax3.set_xlabel('timestep',fontsize=8)
    ax3.set_ylabel('x-position',fontsize=8)
    
    for t in range(len(x)):
        ax3.plot(range(i),x2[t][:i],'r')
    ax3.set_ylim(-20,20)
    ax3.set_xticks(range(0, 20000, 50))
    if (i < 300):
        ax3.set_xlim(0,300)
    else:
        ax3.set_xlim(i-299,i+1)
    
    for tick in ax3.xaxis.get_major_ticks():
        tick.label.set_fontsize(8)
    for tick in ax3.yaxis.get_major_ticks():
        tick.label.set_fontsize(8) 

    ax4.set_ylabel('x-position',fontsize=8)
    
    for t in range(len(x)):
        ax4.plot(range(i),x3[t][:i],'m')
    ax4.set_ylim(-20,20)
    ax4.set_xticks(range(0, 20000, 50))
    if (i < 300):
        ax4.set_xlim(0,300)
    else:
        ax4.set_xlim(i-299,i+1)
    
    for tick in ax4.xaxis.get_major_ticks():
        tick.label.set_fontsize(8)
    for tick in ax4.yaxis.get_major_ticks():
        tick.label.set_fontsize(8)

    plt.savefig("figs2/test_%04d.png"%i,dpi=250)
    
    plt.close(fig)










