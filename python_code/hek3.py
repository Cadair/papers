result = client.query(hek.attrs.Time(tstart, tend), 
                      hek.attrs.EventType("FL"),
                      (hek.attrs.Event.Coord1>50) 
                      or (hek.attrs.FL.PeakFlux>1000.0))