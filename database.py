>>> from sunpy.net import vso
>>> from sunpy.database import Database
>>> database = Database("sqlite:///")
>>> database.download(
...     vso.attrs.Time("2012-08-05", "2012-08-05 00:00:05"),
...     vso.attrs.Instrument('AIA'))
>>> len(database)
2
>>> from sunpy.database.tables import display_entries
>>> print display_entries(
...     database,
...     ["id", "observation_time_start", "wavemin", "wavemax"])
id observation_time_start wavemin wavemax
-- ---------------------- ------- -------
1  2012-08-05 00:00:01    9.4     9.4    
2  2012-08-05 00:00:02    33.5    33.5