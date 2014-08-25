import sunpy
import sunpy.map
aiamap = sunpy.map.Map(sunpy.AIA_171_IMAGE)
smap = aiamap.submap([-1200, -200], [-1000, -0])
smap.peek(draw_grid=True)