"""
Meta-kernel; get the following kernels from
subidirectories spk/planets/, spk/satellites/, lsk/, pck/ of
http://naif.jpl.nasa.gov/pub/naif/generic_kernels/

\begindata
KERNELS_TO_LOAD = (
  'de430.bsp'
  'jup310.bsp'
  'naif0010.tls'
  'pck00010.tpc'
)
ETLO = @1900-01-01T12:00:00
ETHI = @2099-12-31T12:00:00
\begintext
"""

import spice
dot = '.'

### Load kernels
spice.furnsh(dot.join(__file__.split(dot)[:-1] + ['py']))

### Set arguments for Geometry Finder call
### - Times when VENUS crosses equator of Jupiter (Zjup = 0)
### - abcorr='LT+S' - correct for light time and stellar aberration
### - Timestep of 10 days (spice.spd() = seconds per day)
### - nintvls - 450 seems to work here
target, frame, abcorr, obsrvr = 'VENUS', 'IAU_JUPITER', 'LT+S', 'JUPITER'
relate, crdsys, coord = '=', 'RECTANGULAR', 'Z'
refval, adjust, step, nintvls = 0.0, 0.0, spice.spd()*10, 450

### Range of ETs to test
etlo,ethi = [spice.gdpool(s,0,1)[1] for s in 'ETLO ETHI'.split()]
cnfine = spice.wninsd( etlo, ethi, spice.objects.Cell(spice.DataType.SPICE_DP,2))

### Size output
result = spice.objects.Cell(spice.DataType.SPICE_DP,500)

### Make the call to the generic Geometry Finder call
cnfine, result = spice.gfposc( target, frame, abcorr, obsrvr, crdsys, coord, relate, refval, adjust, step, nintvls, cnfine, result )

### Output results
for i in xrange(spice.wncard(result)):
  et0,et1 = spice.wnfetd(result,i)
  assert et0 == et1
  print( ( i, spice.et2utc(et0,'ISOC',3), spice.etcal(et0), spice.spkezr(target,et0,frame,abcorr,obsrvr)[0][2] ,) )
