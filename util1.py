>>> from sunpy import wcs
>>> wcs.convert_hg_hpc(10, 53)
(100.49244115330731, 767.97438321917502)
# Convert that position back to heliographic coordinates
>>> wcs.convert_hpc_hg(100.49, 767.97)
(9.9996521808465175, 52.999563684874893)
# Try to convert a position which is not on the Sun to HG
>>> wcs.convert_hpc_hg(-1500, 0)
sunpy/wcs/wcs.py:180: RuntimeWarning: invalid value encountered in sqrt
  distance = q - np.sqrt(distance)
(nan, nan)
# Convert sky coordinate to a position in HCC
>>> wcs.convert_hpc_hcc(-300, 400, z=True)
(-216716967.63331246, 288956420.9477042, 594364636.2208252)