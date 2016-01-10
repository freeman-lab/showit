# showit

simple and sensible display of images in python, no axes, no interpolation, no frills

### install

```
pip install showit
```

### usage 

####`image`

displays a 2D or 3D array as an image

```python
from numpy import random
from showit import image

im = random.rand(25, 25, 3)
image(im)
```
![](https://s3.amazonaws.com/documentation-samples/showit/image.png)

options

- `cmap` : color map to use (default `gray`)
- `bar` : whether to show a color bar (default `False`)
- `nans` : whether to replace NaNs with 0 (default `True`)
- `clim` : limit for colormap (default `None`)
- `size` : size of figure (default `7`)
- `ax` : an existing axis to plot into (default `None`)

####`tile`

displays many 2D / 3D images as tiles in a grid

```python
from numpy import random
from showit import tile

ims = random.rand(9, 25, 25, 3)
tile(ims)
```
![](https://s3.amazonaws.com/documentation-samples/showit/tile.png)

options

- `cmap` : color map to use (default `gray`)
- `bar` : whether to show a color bar (default `False`)
- `nans` : whether to replace NaNs with 0 (default `True`)
- `clim` : limit for colormap (default `None`)
- `grid` : grid dimensions to use (default is largest square grid)
- `size` : size of figure (default `7`)
- `axis` : which axis to index images with (default `0`)
