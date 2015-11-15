# showit

Simple and sensible display of images

### install

```
pip install showit
```

### usage 

###`image`

displays a 2D or 3D array as an image

```python
from numpy import random
from showit import image

im = random.randn(25, 25)
image(im)
```

options

- `cmap` : color map to use (default `gray`)
- `bar` : whether to show a color bar (default `False`)
- `nans` : whether to replace NaNs with 0 (default `True`)
- `clim` : limit for colormap (default `None`)
- `size` : size of figure (default is largest square grid)
- `ax` : an existing axis to plot into (default `None`)

### usage 

###`tile`

displays many 2D / 3D images as tiles in a grid

```python
from numpy import random
from showit import tile

ims = random.randn(9, 25, 25)
tile(ims)
```

options

- `cmap` : color map to use (default `gray`)
- `bar` : whether to show a color bar (default `False`)
- `nans` : whether to replace NaNs with 0 (default `True`)
- `clim` : limit for colormap (default `None`)
- `grid` : grid dimensions to use (default is largest square grid)
- `size` : size of figure (default is largest square grid)
- `axis` : which axis to index images with (default `0`)
