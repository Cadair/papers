>>> from sunpy.net import vso
>>> client = vso.VSOClient()
>>> tstart, tend = "2011/6/7 05:30", "2011/6/7 10:30"
>>> lasco_query = client.query(vso.attrs.Time(tstart, tend),
...                            vso.attrs.Instrument('lasco'))
>>> lasco_query.num_records()
40
>>> lasco_query.show() 
Start time           End time             Source  Instrument  Type
----------           --------             ------  ----------  ----
2011-06-07 05:35:23  2011-06-07 05:35:48  SOHO    LASCO       CORONA
2011-06-07 05:43:09  2011-06-07 05:43:29  SOHO    LASCO       CORONA
...
>>> pathformat = "/data/{instrument}/{detector}/{file}.fits"
>>> results = client.get(coronagraphs, path = pathformat)