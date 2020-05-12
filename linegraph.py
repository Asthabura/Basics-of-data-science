from matplotlib import pyplot as plt
date_x = [3,4,5,6,7]
open_y = [774.25,776.030029,779.309998,779,779.659973]
plt.plot(date_x,open_y,'c-o',label='open')
high_y = [776.065002,778.710022,782.070007,780.47998,779.659973]
plt.plot(date_x,high_y,'y-o',label='high')
low_y = [769.5,772.890015,775.650024,778.539978,770.75]
plt.plot(date_x,low_y,'g-o',label='low')
close_y = [772.559998,776.429993,776.469971,776.859985,775.08001]
plt.plot(date_x,close_y,'r-o',label='close')
plt.xlabel('Oct2016')
plt.ylabel('Financial data')
plt.title('Financial data of Alphabet Inc.')
plt.grid(True)
plt.legend()
plt.show()
