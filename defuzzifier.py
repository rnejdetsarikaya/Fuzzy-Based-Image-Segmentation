import math
from numpy import log as ln
import numpy as np
from PIL import Image

def inverse_gauss_func(value,mean,std):
	return mean+ math.sqrt(-2*(std**2)*ln(value))


def center_average(result,X,Y,bar):
	bar['value'] = 0
	bar.update()
	final_image = np.zeros((Y,X))
    
	for i in range(1,Y-1):
		if i%10 == 0:
			bar['value'] = i*(100/(Y-1))
			bar.update()
		for j in range(1,X-1):
			mean_e_y = result[j+((X-3)*(i-1))+(i-2)][0]
			mean_e_x = inverse_gauss_func(mean_e_y,0,50)/2
			mean_ne_y = result[j+((X-3)*(i-1))+(i-2)][1]
			mean_ne_x = (inverse_gauss_func(mean_ne_y,255,50)+255)/2
			average = (mean_e_x*mean_e_y+mean_ne_x*mean_ne_y)/(mean_e_y+mean_ne_y)
			if average < 127:
				final_image[i][j] = 255
  
	im = Image.fromarray(final_image)
	im = im.convert("L")
	im.save("output.jpg")
	return final_image
