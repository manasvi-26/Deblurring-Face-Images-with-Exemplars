import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def snr(y, x):
    signal = np.var(x)
    noise = np.mean((y-x)**2)
    return 10*np.log10(signal / noise)

def plot_results(x, k, y, xr):
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) \
        = plt.subplots(2, 3, figsize=(12, 8))
    plt.gray()
    plt.tight_layout()

    ax1.set_title('original')
    ax1.imshow(x)

    ax2.set_title('corrupted')
    ax2.imshow(y)
    ax2.text(0, 0, f'SNR={snr(xr, x):.2f}', horizontalalignment='left',
             verticalalignment='top', bbox=dict(facecolor='white'))
    inset = inset_axes(ax2,
                       width=f'{4*100*k.shape[1]/y.shape[1]}%',
                       height=f'{4*100*k.shape[0]/y.shape[0]}%',
                       loc=3)
    inset.tick_params(labelleft=False, labelbottom=False)
    inset.imshow(k)

    ax3.set_title('reconstructed')
    ax3.imshow(xr)
    ax3.text(0, 0, f'SNR={snr(y, x):.2f}', horizontalalignment='left',
             verticalalignment='top', bbox=dict(facecolor='white'))

    alpha = 2/3
    bins = np.linspace(-50, 50, 200)

    ax4.set_yscale('log')
    ax4.set_ylim((1e0, 2e5))
    ax4.hist(np.diff(x).ravel(), bins=bins)
    ax4.plot(bins, 1e5*np.exp(-np.abs(bins)**alpha))
    ax4.set_xlabel('gradient')
    ax4.set_ylabel('count')

    ax5.set_yscale('log')
    ax5.set_ylim((1e0, 2e5))
    ax5.hist(np.diff(y).ravel(), bins=bins)
    ax5.plot(bins, 1e5*np.exp(-np.abs(bins)**alpha))

    ax6.set_yscale('log')
    ax6.set_ylim((1e0, 2e5))
    ax6.hist(np.diff(xr).ravel(), bins=bins)
    ax6.plot(bins, 1e5*np.exp(-np.abs(bins)**alpha))

    plt.show()