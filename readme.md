List 1: 
[(29.60547057299982, [2160.5304155150002, 2190.135886088]), (28.645026927999879, [2177.958676923, 2206.6037038509999])]

The 29.6 and 28.6 are periods. 2160 and 2190 are times. The flux at 2160 was close enough to the flux at 2190 that they are said to be in the same class. Likewise, the flux at time 2177 was close enough to the flux at time 2206 that they were considered to be in the same class. The grouping is based on relative magnitude of flux. In this case, there are two classes in list 1.

List 2: 
[(2160.4282560649999, 1.000009085066204, 619, 2160.5304155150002, 0.99859591938153613, 624, 2160.6530067210001, 0.99988519379892471, 630), (2177.9382454199999, 0.99981520410864988, 1354, 2177.958676923, 0.99952370911155686, 1355, 2178.0199717300002, 1.0000483210697368, 1358), (2190.0541599940002, 1.0001232637019668, 1891, 2190.135886088, 0.99866017148565545, 1894, 2190.2993382720001, 1.0000638248780793, 1901), (2206.4811145439999, 1.0000503234905507, 2587, 2206.6037038509999, 0.99956234254866916, 2592, 2206.6445670879998, 1.000005168783225, 2594)]

These are our dip zones. They consist of nine element tuples. They are not sorted by class, and so transits belonging to the same planet are not identifiable here. That grouping needs to come from List 1. For any given tuple within List 2 the order of elements is: time at beginning of transit, flux at beginning of transit, index at beginning of transit, time of midtransit, flux at midtransit, index at midtransit, time at end of transit, flux at end of transit, index at end of transit. 

The question is how do we map the grouping structure used in List 1 onto List 2.
