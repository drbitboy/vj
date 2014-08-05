Horizons telnet session to get approximate time of 2014 Venus crossing of Jupiter equator; N.B. change of sign between last two rows of ephemeris table below.

Key is to use BODY (EQUATOR) when asked for frame; ICRF/J2000 later does not matter(?)

- link markdown used to highlight user entries; extra lines added

- I don't know how this translates to the Horizons email or web interface



$ [telnet horizons.jpl.nasa.gov 6775](#)
```
JPL Horizons, version 3.93 
Type `?' for brief intro, `?!' for more details 
System news updated Jul 23, 2014
```
Horizons> [venus](#)
```*******************************************************************************
 Multiple major-bodies match string "VENUS*"

  ID#      Name                               Designation  IAU/aliases/other   
  -------  ---------------------------------- -----------  ------------------- 
        2  Venus Barycenter                                                     
      299  Venus                                                                
     -248  Venus Express Spacecraft                        VEX                  
 
   Number of matches =  3. Use ID# to make unique selection.
*******************************************************************************
```
Select ... [F]tp, [M]ail, [R]edisplay, ?, <cr>: [299](#)
```
*******************************************************************************
 Revised: Jul 31, 2013              Venus                               299 / 2
 
 GEOPHYSICAL DATA (updated 2014-Mar-13):
  Mean radius (km)      =   6051.8(4+-1)  Density (g cm^-3)     =  5.204 
  Mass (10^23 kg )      =     48.685      Flattening, f         =  
  Volume (x10^10 km^3)  =     92.843      Semi-major axis       =  
  Sidereal rot. period  =   -243.0185 d   Rot. Rate (x10^5 s)   = -0.029924 
  Mean solar day        =    116.7490 d   Polar gravity ms^-2   =   
  Mom. of Inertia       =      0.33       Equ. gravity  ms^-2   =  8.870 
  Core radius (km)      =  ~3200          Potential Love # k2   = ~0.25 

  Grav spectral fact u  =      1.5        Topo. spectral fact t =  23       
  Fig. offset (Rcf-Rcm) =      0.19+-01   Offset (lat./long.)   = 11/102 dg/dg 
  GM (km^3 s^-2)        = 324858.63       Equatorial Radius, Re = 6051.893 km 
  GM 1-sigma (km^3 s^-2)=    +-0.04       Mass ratio (Sun/Venus)= 408523.72
  
  Atmos. pressure (bar) =    90           Max. angular diam.    =   60.2" 
  Mean Temperature (K)  =  735            Visual mag. V(1,0)    =   -4.40 
  Geometric albedo      =    0.65         Obliquity to orbit    =  177.3 deg 
  Sidereal orb. per.    =    0.61519726 y Orbit vel.  km/s      =   35.0214 
  Sidereal orb. per.    =  224.70079922 d Escape vel. km/s      =   10.361 
  Hill's sphere rad. Rp =  167.1          Planetary Solar Const = 2613.9 (Wm^2) 
*******************************************************************************
 ```
 Select ... [E]phemeris, [F]tp, [M]ail, [R]edisplay, ?, <cr>: [e](#)
 
 Observe, Elements, Vectors  [o,e,v,?] : [v](#)
 
 Coordinate center [ <id>,coord,geo  ] : [500@599](#)
```
   #   E. Lon    DXY      DZ    Observatory Name
  --- -------- ------- -------  ----------------
  500   0.0000 +000000  000000  Jupiter (body center)
 ```
Confirm selected station    [ y/n ] --> [y](#)

Reference plane [eclip, frame, body ] : [body](#)

Starting CT  [>=   1799-Dec-18 00:00] : [2014-12-23 00:00](#)

Ending   CT  [<=   2200-Jan-14 00:00] : [2014-12-23 06:00](#)  

Output interval [ex: 10m, 1h, 1d, ? ] : [10m](#)
```
 Current output table defaults --
   Ref. Frame   = ICRF/J2000.0
   Corrections  = NONE
   Units        = AU-D
   CSV format   = NO
   Table type   = 03 (position, velocity, LT, rng, rng-rate)
   Vector label = NO
```
Accept default output [ cr=(y), n, ?] : [n](#)

Output reference frame [J2000, B1950] : [j2000](#)

Corrections [ 1=NONE, 2=LT, 3=LT+S ]  : [1](#)

Output units [1=KM-S, 2=AU-D, 3=KM-D] : [1](#)

Spreadsheet CSV format    [ YES, NO ] : [y](#)

Label cartesian output    [ YES, NO ] : [y](#)

Select output table type  [ 1-6, ?  ] : [1](#)
```
Working ... /  
*******************************************************************************
Ephemeris / PORT_LOGIN Tue Aug  5 08:19:10 2014 Pasadena, USA    / Horizons    
*******************************************************************************
Target body name: Venus (299)                     {source: DE-0431LE-0431}
Center body name: Jupiter (599)                   {source: JUP310}
Center-site name: BODY CENTER
*******************************************************************************
Start time      : A.D. 2014-Dec-23 00:00:00.0000 CT 
Stop  time      : A.D. 2014-Dec-23 06:00:00.0000 CT 
Step-size       : 10 minutes
*******************************************************************************
Center geodetic : 0.00000000,0.00000000,0.0000000 {E-lon(deg),Lat(deg),Alt(km)}
Center cylindric: 0.00000000,0.00000000,0.0000000 {E-lon(deg),Dxy(km),Dz(km)}
Center pole/equ : IAU_JUPITER                     {East-longitude -}
Center radii    : 71492.0 x 71492.0 x 66854.0 km  {Equator, meridian, pole}    
Output units    : KM-S                                                         
Output format   : 01
Output type     : GEOMETRIC cartesian states
Coordinate systm: Body Mean Equator and Node of Date                           
*******************************************************************************
JDCT ,   , X, Y, Z,
*******************************************************************************
$$SOE
2457014.500000000, A.D. 2014-Dec-23 00:00:00.0000,  6.328358274962267E+08, -6.445093030399079E+08,  6.839306818190792E+04,
[...]
2457014.729166667, A.D. 2014-Dec-23 05:30:00.0000,  6.335704645935713E+08, -6.439251896182678E+08,  5.251279676634309E+03,
2457014.736111111, A.D. 2014-Dec-23 05:40:00.0000,  6.335926843133754E+08, -6.439074333314494E+08,  3.339494072877278E+03,
2457014.743055556, A.D. 2014-Dec-23 05:50:00.0000,  6.336149015512241E+08, -6.438896737638450E+08,  1.427803342235988E+03,
2457014.750000000, A.D. 2014-Dec-23 06:00:00.0000,  6.336371163062121E+08, -6.438719109160609E+08, -4.837924605347944E+02,
$$EOE
*******************************************************************************
Coordinate system description:

  Body Mean Equator and Node of Date

    Reference epoch: "of date"
    Reference plane: ICRF/J2000.0
    xy-plane: central-body mean equator plane at reference epoch
    x-axis  : out along the ascending node of the central-body mean equator
              plane on the reference plane at the reference epoch
    z-axis  : along the central-body mean north pole at the reference epoch

Symbol meaning  

    JDCT     Epoch Julian Date, Coordinate Time
      X      x-component of position vector (km)                               
      Y      y-component of position vector (km)                               
      Z      z-component of position vector (km)                               

Geometric states/elements have no aberration corrections applied.

 Computations by ...
     Solar System Dynamics Group, Horizons On-Line Ephemeris System
     4800 Oak Grove Drive, Jet Propulsion Laboratory
     Pasadena, CA  91109   USA
     Information: http://ssd.jpl.nasa.gov/
     Connect    : telnet://ssd.jpl.nasa.gov:6775  (via browser)
                  telnet ssd.jpl.nasa.gov 6775    (via command-line)
     Author     : Jon.Giorgini@jpl.nasa.gov
*******************************************************************************
 >>> Select... [A]gain, [N]ew-case, [F]tp, [K]ermit, [M]ail, [R]edisplay, ? : **q**
                                                                          
     ___    _____     ___                                                 
    /_ /|  /____/ \  /_ /|       Horizons On-line Ephemeris System v3.93  
    | | | |  __ \ /| | | |       Solar System Dynamics Group              
 ___| | | | |__) |/  | | |__     Jet Propulsion Laboratory                
/___| | | |  ___/    | |/__ /|   Pasadena, CA, USA                        
|_____|/  |_|/       |_____|/                                             
 
Connection closed by foreign host.
```
