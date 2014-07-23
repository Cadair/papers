>>> from sunpy.net.helio import hec
>>> hc = hec.Client()
>>> tstart, tend = "2011-06-07T06:00:00", "2011-06-07T12:00:00"
>>> event_type = "cme"

# From all the catalogues these which name contain our event of interest
>>> catalogues = hc.get_table_names()
>>> catalogues_event = [l[0] for l in catalogues 
...                     if event_type in l[0] and 'list' not in l[0]]

# Query all the catalogues that comes from cactus
>>> results = [hc.time_query(tstart, tend, event) 
...            for event in catalogues_event if 'cactus' in event]
>>> for cat in results:
...     print "{cat} has {nres} results".format(cat = cat.ID, \
...                                             nres = len(cat.array))
__helio_hec-cactus_stereoa_cme has 4 results
__helio_hec-cactus_stereob_cme has 3 results
__helio_hec-cactus_soho_cme has 7 results