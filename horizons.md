Horizons telnet session to get approximate time of 2014 Venus crossing of Jupiter equator.

Key is to use BODY (EQUATOR) when asked for frame; ICRF/J2000 later does not matter(?)

- link markdown used to highlight user entries

- I don't know how this translates to the Horizons email or web interface


```
$ [telnet horizons.jpl.nasa.gov 6775](#)

JPL Horizons, version 3.93 
Type `?' for brief intro, `?!' for more details 
System news updated Jul 23, 2014
 
Horizons> [venus](#)
*******************************************************************************
 Multiple major-bodies match string "VENUS*"

  ID#      Name                               Designation  IAU/aliases/other   
  -------  ---------------------------------- -----------  ------------------- 
        2  Venus Barycenter                                                     
      299  Venus                                                                
     -248  Venus Express Spacecraft                        VEX                  
 
   Number of matches =  3. Use ID# to make unique selection.
*******************************************************************************
 Select ... [F]tp, [M]ail, [R]edisplay, ?, <cr>: ```[299](#)```
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
 Select ... [E]phemeris, [F]tp, [M]ail, [R]edisplay, ?, <cr>: [e](#)
 
 Observe, Elements, Vectors  [o,e,v,?] : [v](#)
 Coordinate center [ <id>,coord,geo  ] : [500@599](#)

   #   E. Lon    DXY      DZ    Observatory Name
  --- -------- ------- -------  ----------------
  500   0.0000 +000000  000000  Jupiter (body center)
 
 Confirm selected station    [ y/n ] --> [y](#)
 Reference plane [eclip, frame, body ] : [body](#)
 Starting CT  [>=   1799-Dec-18 00:00] : [2014-12-23 00:00](#)
 Ending   CT  [<=   2200-Jan-14 00:00] : [2014-12-23 06:00](#)           
 Output interval [ex: 10m, 1h, 1d, ? ] : [10m](#)
 
 Current output table defaults --
   Ref. Frame   = ICRF/J2000.0
   Corrections  = NONE
   Units        = AU-D
   CSV format   = NO
   Table type   = 03 (position, velocity, LT, rng, rng-rate)
   Vector label = NO
 
 Accept default output [ cr=(y), n, ?] : [n](#)
 Output reference frame [J2000, B1950] : [j2000](#)
 Corrections [ 1=NONE, 2=LT, 3=LT+S ]  : [1](#)
 Output units [1=KM-S, 2=AU-D, 3=KM-D] : [1](#)
 Spreadsheet CSV format    [ YES, NO ] : [y](#)
 Label cartesian output    [ YES, NO ] : [y](#)
 Select output table type  [ 1-6, ?  ] : [1](#)
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
2457014.506944444, A.D. 2014-Dec-23 00:10:00.0000,  6.328581286028197E+08, -6.444916553093809E+08,  6.647818265101289E+04,
2457014.513888889, A.D. 2014-Dec-23 00:20:00.0000,  6.328804272578822E+08, -6.444740042823417E+08,  6.456339017567653E+04,
2457014.520833333, A.D. 2014-Dec-23 00:30:00.0000,  6.329027234605114E+08, -6.444563499591451E+08,  6.264869081035574E+04,
2457014.527777778, A.D. 2014-Dec-23 00:40:00.0000,  6.329250172097980E+08, -6.444386923401551E+08,  6.073408461095733E+04,
2457014.534722222, A.D. 2014-Dec-23 00:50:00.0000,  6.329473085048349E+08, -6.444210314257406E+08,  5.881957163215202E+04,
2457014.541666667, A.D. 2014-Dec-23 01:00:00.0000,  6.329695973447083E+08, -6.444033672162793E+08,  5.690515192913057E+04,
2457014.548611111, A.D. 2014-Dec-23 01:10:00.0000,  6.329918837285024E+08, -6.443856997121570E+08,  5.499082555786004E+04,
2457014.555555556, A.D. 2014-Dec-23 01:20:00.0000,  6.330141676553019E+08, -6.443680289137634E+08,  5.307659257210209E+04,
2457014.562500000, A.D. 2014-Dec-23 01:30:00.0000,  6.330364491241858E+08, -6.443503548214995E+08,  5.116245302828467E+04,
2457014.569444444, A.D. 2014-Dec-23 01:40:00.0000,  6.330587281342338E+08, -6.443326774357717E+08,  4.924840698097557E+04,
2457014.576388889, A.D. 2014-Dec-23 01:50:00.0000,  6.330810046845229E+08, -6.443149967569940E+08,  4.733445448539389E+04,
2457014.583333333, A.D. 2014-Dec-23 02:00:00.0000,  6.331032787741286E+08, -6.442973127855883E+08,  4.542059559625786E+04,
2457014.590277778, A.D. 2014-Dec-23 02:10:00.0000,  6.331255504021242E+08, -6.442796255219847E+08,  4.350683036933510E+04,
2457014.597222222, A.D. 2014-Dec-23 02:20:00.0000,  6.331478195675832E+08, -6.442619349666198E+08,  4.159315885977815E+04,
2457014.604166667, A.D. 2014-Dec-23 02:30:00.0000,  6.331700862695773E+08, -6.442442411199390E+08,  3.967958112216962E+04,
2457014.611111111, A.D. 2014-Dec-23 02:40:00.0000,  6.331923505071776E+08, -6.442265439823937E+08,  3.776609721181472E+04,
2457014.618055556, A.D. 2014-Dec-23 02:50:00.0000,  6.332146122794536E+08, -6.442088435544455E+08,  3.585270718389479E+04,
2457014.625000000, A.D. 2014-Dec-23 03:00:00.0000,  6.332368715854759E+08, -6.441911398365618E+08,  3.393941109352811E+04,
2457014.631944444, A.D. 2014-Dec-23 03:10:00.0000,  6.332591284243143E+08, -6.441734328292181E+08,  3.202620899564285E+04,
2457014.638888889, A.D. 2014-Dec-23 03:20:00.0000,  6.332813827950366E+08, -6.441557225329000E+08,  3.011310094575409E+04,
2457014.645833333, A.D. 2014-Dec-23 03:30:00.0000,  6.333036346967144E+08, -6.441380089480963E+08,  2.820008699804760E+04,
2457014.652777778, A.D. 2014-Dec-23 03:40:00.0000,  6.333258841284163E+08, -6.441202920753082E+08,  2.628716720843434E+04,
2457014.659722222, A.D. 2014-Dec-23 03:50:00.0000,  6.333481310892134E+08, -6.441025719150418E+08,  2.437434163139680E+04,
2457014.666666667, A.D. 2014-Dec-23 04:00:00.0000,  6.333703755781749E+08, -6.440848484678137E+08,  2.246161032280426E+04,
2457014.673611111, A.D. 2014-Dec-23 04:10:00.0000,  6.333926175943750E+08, -6.440671217341448E+08,  2.054897333638149E+04,
2457014.680555556, A.D. 2014-Dec-23 04:20:00.0000,  6.334148571368846E+08, -6.440493917145669E+08,  1.863643072829358E+04,
2457014.687500000, A.D. 2014-Dec-23 04:30:00.0000,  6.334370942047788E+08, -6.440316584096183E+08,  1.672398255325726E+04,
2457014.694444444, A.D. 2014-Dec-23 04:40:00.0000,  6.334593287971336E+08, -6.440139218198445E+08,  1.481162886600388E+04,
2457014.701388889, A.D. 2014-Dec-23 04:50:00.0000,  6.334815609130245E+08, -6.439961819458009E+08,  1.289936972218708E+04,
2457014.708333333, A.D. 2014-Dec-23 05:00:00.0000,  6.335037905515318E+08, -6.439784387880480E+08,  1.098720517612071E+04,
2457014.715277778, A.D. 2014-Dec-23 05:10:00.0000,  6.335260177117360E+08, -6.439606923471558E+08,  9.075135283230396E+03,
2457014.722222222, A.D. 2014-Dec-23 05:20:00.0000,  6.335482423927211E+08, -6.439429426237005E+08,  7.163160098098684E+03,
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
