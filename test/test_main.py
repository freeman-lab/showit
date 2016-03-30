from numpy import random
import matplotlib
from showit import image, tile

matplotlib.use('Agg')

def test_image():
	im = random.randn(25, 25)
	image(im)

def test_tile():
	im = random.randn(5, 25, 25)
	tile(im)