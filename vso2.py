>>> condition = (vso.attrs.Detector("cor1") |
...              vso.attrs.Wave(125, 135) |
...              vso.attrs.Wave(165, 175) ) # in angstroms
>>> advanced = client.query(vso.attrs.Time(tstart, tend), condition)
>>> advanced.num_records()
4434
>>> advanced.show()
Start time           End time             Source    Instrument  Type
----------           --------             ------    ----------  ----
2011-06-07 00:00:00  2011-06-08 00:00:00  SDO       EVE         FULLDISK
...
2011-06-07 05:31:09  2011-06-07 05:31:19  PROBA2    SWAP        FULLSUN
...
2011-06-07 10:25:43  2011-06-07 10:25:45  STEREO_B  SECCHI      CORONA
2011-06-07 10:30:00  2011-06-07 10:30:01  STEREO_A  SECCHI      CORONA
...
2011-06-07 10:30:00  2011-06-07 10:30:01  SDO       AIA         FULLDISK