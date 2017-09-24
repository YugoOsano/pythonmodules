
#--- For graph plot driven by generation of file by 
#    an ongoing simulation, non-blocking plot of matplotlib will be
#    used with inotify-tools (bash script with inotifywait command) 

# http://stackoverflow.com/questions/11874767/real-time-plotting-in-while-loop-with-matplotlib
# http://stackoverflow.com/questions/5541594/matplotlib-draw-showing-nothing

# matplotlib install into Ubuntu
# sudo apt-get install python-matplotlib
# sudo apt-get install python3-matplotlib python3-gi-cairo

# https://www.trifields.jp/how-to-install-matplotlib-in-ubuntu-14-04-and-python-3-1173

# for scikit-learn,
# sudo apt-get install python3-sklearn

import matplotlib.pyplot as plt

plt.ion()
plt.figure()

plt.xlim(-1,10)
plt.ylim(-1,10)

for i in range(10):
    for j in range(10):
        plt.plot([i], [j], 'o')
        plt.draw()

plt.show(block=True) # see StackOverFlow:12358312
#raw_input("done >>")  

