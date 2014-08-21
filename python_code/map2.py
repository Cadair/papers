import sunpy.map
import matplotlib.pyplot as plt
compmap = sunpy.map.Map(sunpy.AIA_171_IMAGE, sunpy.RHESSI_IMAGE, 
                         composite=True)
compmap.set_levels(1, range(0, 50, 5), percent=True)
compmap.set_colors(1, "Reds_r")
#Plot the result and crop
ax = plt.subplot()
compmap.plot()
ax.axis([200, 600, -600, -200])
plt.show()