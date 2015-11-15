# showit

Simple and sensible display of images

### install

```
pip install showit
```

### image

displays a 2D or 3D array as an image

```
from numpy import random
from showit import image

im = random.randn(25, 25)
image(im)
```

options

####`cmap`
Color map to use (default `gray`)

####`bar`
Whether to show a color bar (default `False`)

####`nans`
Whether to replace NaNs with 0 (default `True`)

####`clim`
Limit for colormap (default `None`)

####`size`
Size of figure (default is largest square grid)

####`ax`
An existing axis to plot into


### tile

displays many 2D / 3D images as tiles in a grid

```python
from numpy import random
from showit import tile

ims = random.randn(9, 25, 25)
tile(ims)
```

options

####`cmap`
Color map to use (default `gray`)

####`bar`
Whether to show a color bar (default `False`)

####`nans`
Whether to replace NaNs with 0 (default `True`)

####`clim`
Limit for colormap (default `None`)

####`grid`
Grid dimensions to use (default is largest square grid)

####`size`
Size of figure (default is largest square grid)

####`size`
Size of figure (default is largest square grid)

####`axis`
Which axis to index images with
