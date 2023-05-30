# pip install Pillow
# pip install numba
# pip install np

from PIL import Image, ImageDraw
from numba import jit
import numpy as np

def mandelbrot_simple(c, maxiter):
	n, z = 0, 0
	while abs(z) <= 2 and n < maxiter:
		n, z = n + 1, z*z + c
	return n

@jit
def mandelbrot_optimized(creal, cimag, maxiter):
	real, imag = creal, cimag
	for n in range(maxiter):
		real2, imag2 = real * real, imag * imag
		if real2 + imag2 > 4.0:
			return n
		imag = 2 * real * imag + cimag
		real = real2 - imag2 + creal       
	return maxiter

@jit
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
	r1 = np.linspace(xmin, xmax, width)
	r2 = np.linspace(ymin, ymax, height)
	result = np.empty((width,height))
	for i in range(width):
		for j in range(height):
			result[i,j] = mandelbrot_optimized(r1[i], r2[j], maxiter)
	return result

def draw_set(result, width, height, maxiter):
	im = Image.new('HSV', (width, height), (0, 0, 0))
	draw = ImageDraw.Draw(im)
	for x in range(width):
		for y in range(height):
			m = result[x][y]
			hue = int(255 * m / maxiter)
			saturation = 255
			value = 255 if m < maxiter else 0
			draw.point([x, y], (hue, saturation, value))
	return im

WIDTH = 1024
HEIGHT = 1024
MAX_ITER = 2 ** 12
#X_MIN, X_MAX, Y_MIN, Y_MAX = -2, 0.5, -1.25, 1.25 # the full set
X_MIN, X_MAX, Y_MIN, Y_MAX = -0.74877, -0.74872, 0.065053, 0.065103 # interesting detail

result = mandelbrot_set(X_MIN, X_MAX, Y_MIN, Y_MAX, WIDTH, HEIGHT, MAX_ITER)
im = draw_set(result, WIDTH, HEIGHT, MAX_ITER)
im.convert('RGB').save(f'mandelbrot_{X_MIN}_{X_MAX}_{Y_MIN}_{Y_MAX}_{WIDTH}_{HEIGHT}_{MAX_ITER}.png', 'PNG')
