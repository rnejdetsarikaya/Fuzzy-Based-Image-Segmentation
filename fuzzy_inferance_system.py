import fuzzifier as fz
import numpy as np

rule_dict = {"low-low":"NE","medium-low":"E","high-low":"NE","low-high":"NE","medium-high":"NE","high-high":"NE"}



def rule_base(mean,std,label):
    return rule_dict[label],min(mean,std)


def fis(means,stds,X,Y,bar):
	bar['value'] = 0
	bar.update()
	result = []
	min_ = min(stds)
	max_ = max(stds)

	for i in range(1,Y-1):
		if i%10 == 0:
			bar['value'] = i*(100/(Y-1))
			bar.update()           
		for j in range(1,X-1):

            		mean = means[j+((X-3)*(i-1))+(i-2)]
            		std = stds[j+((X-3)*(i-1))+(i-2)]

            		mean_low = fz.gaussmf(mean, 0, 50)#mean_mf(mean,"low")
            		mean_medium = fz.gaussmf(mean, 127, 50)#mean_mf(mean,"medium")            
            		mean_high = fz.gaussmf(mean, 255, 50)#mean_mf(mean,"high")
            		std_low = fz.gaussmf(std, min_, 3)#std_mf(std,"low")
            		std_high = fz.gaussmf(std,max_, 20)#std_mf(std,"high") 
            
			#Rules
            		rule1, value1 = rule_base(mean_low,std_low,"low-low")
            		rule2, value2 = rule_base(mean_medium,std_low,"medium-low")#value2 -> max E değeri tuple(E,NE)-> (value2,?)
            		rule3, value3 = rule_base(mean_high,std_low,"high-low")
            		rule4, value4 = rule_base(mean_low,std_high,"low-high")
            		rule5, value5 = rule_base(mean_medium,std_high,"medium-high")
            		rule6, value6 = rule_base(mean_high,std_high,"high-high")
            		result.append((value2,max(value1,value3,value4,value5,value6)))
                      
	print('bitti')            
	return result
            
            
