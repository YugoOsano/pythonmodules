
#--- For graph plot driven by generation of file by 
#    an ongoing simulation, non-blocking plot of matplotlib will be
#    used with inotify-tools (bash script with inotifywait command) 

# http://stackoverflow.com/questions/11874767/real-time-plotting-in-while-loop-with-matplotlib
# http://stackoverflow.com/questions/5541594/matplotlib-draw-showing-nothing

import matplotlib.pyplot as plt

plt.ion()
plt.figure()

plt.xlim(-1,10)
plt.ylim(-1,10)

for i in range(10):
    for j in range(10):
        plt.plot([i], [j], 'o')
        plt.draw()
raw_input("done >>")  

