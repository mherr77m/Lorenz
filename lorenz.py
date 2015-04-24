# Creates frames for a Lorenz Model animation.
# Use ffmpeg to create animation from frames.

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

def run_ens(xi,yi,zi,ens_num,stepCnt,dt):
    x = []
    y = []
    z = []

    for t in range(ens_num):
        
        xs = np.empty((stepCnt + 1,))
        ys = np.empty((stepCnt + 1,))
        zs = np.empty((stepCnt + 1,))
    
        # Setting initial values
        mean = 0
        sdev = .5
        xs[0], ys[0], zs[0] = (xi+random.normalvariate(mean, sdev), 
                               yi+random.normalvariate(mean, sdev), 
                               zi+random.normalvariate(mean, sdev))

        for i in range(stepCnt) :
            x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
            xs[i + 1] = xs[i] + (x_dot * dt)
            ys[i + 1] = ys[i] + (y_dot * dt)
            zs[i + 1] = zs[i] + (z_dot * dt)

        x.append(xs)
        y.append(ys)
        z.append(zs)

    return x,y,z

dt = 0.01
stepCnt = 20000

#--------------
# Control Run
#--------------
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

#--------------
# Ensemble Runs
#--------------
xi = -15.7
yi = -6.5
zi = 44
ens_num=20

x_grn,y_grn,z_grn = run_ens(xi,yi,zi,ens_num,stepCnt,dt)

xi = .14
yi = .32
zi = 13.6

x_red,y_red,z_red = run_ens(xi,yi,zi,ens_num,stepCnt,dt)

xi = -9
yi = -4
zi = 33

x_mag,y_mag,z_mag = run_ens(xi,yi,zi,ens_num,stepCnt,dt)

#--------------
# Plot Frames
#--------------
frames = 1000
for i in range(frames):
    fig = plt.figure(figsize=(10,5))
    gs2 = gridspec.GridSpec(3, 4)
    gs2.update(left=0.0, right=0.95, hspace=0.2)
    ax = plt.subplot(gs2[:, :-2],projection='3d')
    ax2 = plt.subplot(gs2[0, -2:])
    ax3 = plt.subplot(gs2[2, -2:])
    ax4 = plt.subplot(gs2[1, -2:])
 
    # Plots
    ax.set_title("Lorenz Attractor")
    ax.set_xlabel("X Axis",fontsize=8)
    ax.set_ylabel("Y Axis",fontsize=8)
    ax.set_zlabel("Z Axis",fontsize=8)
    ax.scatter(xs[:], ys[:], zs[:],'grey',s=1,edgecolor='none')
    for t in range(len(x_grn)):
        if i < 300:
            ax.plot(x_grn[t][:i], y_grn[t][:i], z_grn[t][:i],'g',linewidth=.5)
            ax.plot(x_red[t][:i], y_red[t][:i], z_red[t][:i],'r',linewidth=.5)
            ax.plot(x_mag[t][:i], y_mag[t][:i], z_mag[t][:i],'m',linewidth=.5)
        else:
            ax.plot(x_grn[t][i-299:i], y_grn[t][i-299:i], \
                    z_grn[t][i-299:i],'g',linewidth=.5)
            ax.plot(x_red[t][i-299:i], y_red[t][i-299:i], \
                    z_red[t][i-299:i],'r',linewidth=.5)
            ax.plot(x_mag[t][i-299:i], y_mag[t][i-299:i], \
                    z_mag[t][i-299:i],'m',linewidth=.5)

    # Plot Formatting
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
    for t in range(len(x_grn)):
        ax2.plot(range(i),x_grn[t][:i],'g')
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
    for t in range(len(x_red)):
        ax3.plot(range(i),x_red[t][:i],'r')
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
    for t in range(len(x_mag)):
        ax4.plot(range(i),x_mag[t][:i],'m')
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

    plt.savefig("figs4/test_%04d.png"%i,dpi=250)
    
    plt.close(fig)










