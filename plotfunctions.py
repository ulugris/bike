from matplotlib import pyplot as plt
from numpy import degrees, sin, cos

fg1 = plt.figure()
ax1 = fg1.add_axes([0.1, 0.1, 0.85, 0.85])

dts = plt.Line2D((0, 0), (0, 1), ls='', color='black', marker=".", ms=20)
chs = plt.Line2D((0, 0), (0, 0), lw=4, color='tab:orange')


def plot_response(T, X, Xo=None):
    fig = plt.figure()

    aa = fig.add_axes([0, 0, 1, 1])
    aa.plot([0, T[-1]], [0, 0], lw=1, alpha=0.25, color='tab:blue')
    if Xo is not None:
        aa.plot(T, [degrees(a) for a in Xo[0]], color='tab:blue', ls=':')
    aa.plot(T, [degrees(a) for a in X[0]], color='tab:blue')        
    aa.set_ylabel(r'$\varphi$ (deg)', color='tab:blue')

    aa.set_xlabel('Tiempo (s)')
    aa.set_xlim([0, T[-1]])

    plt.show()


def plot_steering(T, u):
    fig = plt.figure()

    ax = fig.add_axes([0, 0, 1, 1])

    ax.plot(T, degrees(u), color='tab:blue')
    ax.set_ylabel(r'$u$ (deg)')

    ax.set_xlabel('Tiempo (s)')
    ax.set_xlim([0, T[-1]])

    plt.show()


def init():
    plt.rcParams['animation.html'] = 'html5'

    ax1.plot((-1, 1), (0, 0), color='tab:gray', lw=1)

    ax1.axis('scaled')
    ax1.set_xlim((-0.5, 0.5))
    ax1.set_ylim((-0.05, 1.05))

    ax1.add_line(chs)
    ax1.add_line(dts)

    return dts, chs


def anim(i, Y, dt, h):
    dts.set_xdata((0, h*sin(Y[0, i])))
    dts.set_ydata((0, h*cos(Y[0, i])))

    chs.set_xdata((0, h*sin(Y[0, i])))
    chs.set_ydata((0, h*cos(Y[0, i])))

    return dts, chs
