from numpy import ndarray, rollaxis, asarray, nan_to_num, ceil, sqrt, around

def tile(imgs, cmap='gray', bar=False, nans=True, clim=None, grid=None, size=9, axis=0, fig=None):
    """
    Display a collection of images as a grid of tiles

    Parameters
    ----------
    img : list or ndarray (2D or 3D)
        The images to display. Can be a list of either 2D, 3D,
        or a mix of 2D and 3D numpy arrays. Can also be a single
        numpy array, in which case the axis parameter will be assumed
        to index the image list, e.g. a (10, 512, 512) array with axis=0 
        will be treated as 10 different (512,512) images, and the same
        array with axis=1 would be treated as 512 (10,512) images.

    cmap : str or Colormap or list, optional, default = 'gray'
        A colormap to use, for non RGB images, a list can be used to
        specify a different colormap for each image

    bar : boolean, optional, default = False
        Whether to append a colorbar to each image

    nans : boolean, optional, deafult = True
        Whether to replace NaNs, if True, will replace with 0s

    clim : tuple or list of tuples, optional, default = None
        Limits for scaling image, a list can be used to
        specify different limits for each image

    grid : tuple, optional, default = None
        Dimensions of image tile grid, if None, will use a square grid
        large enough to include all images

    size : scalar, optional, deafult = 11
        Size of the figure

    axis : int, optional, default = 0
        Which axis of array indexes images

    fig : matplotlib figure, optional, default = None
        An existing figure to plot on
    """
    from matplotlib.pyplot import figure, colorbar
    from mpl_toolkits.axes_grid1 import ImageGrid

    if not isinstance(imgs, list):
        if not isinstance(imgs, ndarray):
            imgs = asarray(imgs)        
        if (axis < 0) | (axis >= imgs.ndim):
            raise ValueError("Must specify a valid axis to index the images")
        imgs = list(rollaxis(imgs, axis, 0))

    imgs = [asarray(im) for im in imgs]

    if (nans is True) and (imgs[0].dtype != bool):
        imgs = [nan_to_num(im) for im in imgs]

    if fig is None:
        fig = figure(figsize=(size, size))

    if bar is True:
        axes_pad = 0.4
        if sum([im.ndim == 3 for im in imgs]):
            raise ValueError("Cannot show meaningful colorbar for RGB image")
        cbar_mode = "each"
    else:
        axes_pad = 0.2
        cbar_mode = None

    nimgs = len(imgs)

    if not isinstance(cmap, list):
        cmap = [cmap for _ in range(nimgs)]

    if not isinstance(clim, list):
        clim = [clim for _ in range(nimgs)]
    
    if len(clim) < nimgs:
        raise ValueError("Number of clim specifications %g too small for number of images %g"
                         % (len(clim), nimgs))

    if len(cmap) < nimgs:
        raise ValueError("Number of cmap specifications %g too small for number of images %g"
                         % (len(cmap), nimgs))

    if grid is None:
        c = int(ceil(sqrt(nimgs)))
        grid = (c, c)

    ngrid = grid[0] * grid[1]
    if ngrid < nimgs:
        raise ValueError("Total grid count %g too small for number of images %g" % (ngrid, nimgs))

    g = ImageGrid(fig, 111, nrows_ncols=grid, axes_pad=axes_pad,
                  cbar_mode=cbar_mode, cbar_size="5%", cbar_pad="5%")

    axes = []
    for i, im in enumerate(imgs):
        ax = g[i].imshow(im, cmap=cmap[i], interpolation='nearest', clim=clim[i])
        g[i].axis('off')

        if bar:
            cb = colorbar(ax, g[i].cax)
            rng = abs(cb.vmax - cb.vmin) * 0.05
            cb.set_ticks([around(cb.vmin + rng, 1), around(cb.vmax - rng, 1)])
            cb.outline.set_visible(False)

        axes.append(ax)

    if nimgs < ngrid:
        for i in range(nimgs, ngrid):
            g[i].axis('off')
            g[i].cax.axis('off')

    return axes, g

def image(img, cmap='gray', bar=False, nans=True, clim=None, size=7, ax=None):
    """
    Streamlined display of images using matplotlib.

    Parameters
    ----------
    img : ndarray, 2D or 3D
        The image to display

    cmap : str or Colormap, optional, default = 'gray'
        A colormap to use, for non RGB images

    bar : boolean, optional, default = False
        Whether to append a colorbar

    nans : boolean, optional, deafult = True
        Whether to replace NaNs, if True, will replace with 0s

    clim : tuple, optional, default = None
        Limits for scaling image

    size : scalar, optional, deafult = 9
        Size of the figure

    ax : matplotlib axis, optional, default = None
        An existing axis to plot into
    """
    from matplotlib.pyplot import axis, colorbar, figure, gca

    img = asarray(img)

    if (nans is True) and (img.dtype != bool):
        img = nan_to_num(img)

    if ax is None:
        f = figure(figsize=(size, size))
        ax = gca()

    if img.ndim == 3:
        if bar:
            raise ValueError("Cannot show meaningful colorbar for RGB images")
        if img.shape[2] != 3:
            raise ValueError("Size of third dimension must be 3 for RGB images, got %g" % img.shape[2])
        mn = img.min()
        mx = img.max()
        if mn < 0.0 or mx > 1.0:
            raise ValueError("Values must be between 0.0 and 1.0 for RGB images, got range (%g, %g)" % (mn, mx))
        im = ax.imshow(img, interpolation='nearest', clim=clim)
    else:
        im = ax.imshow(img, cmap=cmap, interpolation='nearest', clim=clim)

    if bar is True:
        cb = colorbar(im, fraction=0.046, pad=0.04)
        rng = abs(cb.vmax - cb.vmin) * 0.05
        cb.set_ticks([around(cb.vmin + rng, 1), around(cb.vmax - rng, 1)])
        cb.outline.set_visible(False)

    axis('off')

    return im
