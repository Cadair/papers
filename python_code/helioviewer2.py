import sunpy.map
filepath = hv.download_jp2("2012/07/05 00:30:00",
                            observatory='SDO',
                            instrument="HMI", detector="HMI", 
                            measurement="continuum")
sunpy.map.Map(filepath).submap([200, 550], [-400, -200]).peek()