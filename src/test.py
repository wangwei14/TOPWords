#coding:utf-8  
import matplotlib  
# matplotlib.use('qt4agg')  
from matplotlib.font_manager import *  
import matplotlib.pyplot as plt  
#定义自定义字体，文件名从1.b查看系统中文字体中来  
myfont = FontProperties(fname='/usr/share/fonts/msyh.ttf/msyh.ttf')  
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus']=False  
plt.plot([-1,2,-5,3])  
plt.title(u'中文',fontproperties=myfont)  
plt.show()
