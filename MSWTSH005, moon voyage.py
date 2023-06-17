from vpython import *

##objects

earth=sphere(pos=vector(0,0,0),radius=6.4e6,color=color.blue,opacity=1)
moon=sphere(pos=vector(4.0e8,0,0),radius=1.75e6,color=color.white)
craft=sphere(pos=vector(-0.5*(50000+6.4e6+1.0e6),sqrt(3)*(50000+6.4e6+1.0e6)/2,0),radius=1.0e6,color=color.red)
craft.trail=curve(pos=craft.pos,color=craft.color)

##constants

G=6.67e-11
earth.M=6.0e24
moon.M=7.0e22
craft.M=175.0
dt=10
t=0
    
## These two while-loops execute the one orbit around the earth.
while t<=6400:##t=6400 is the time after one orbit around the earth.
    R=vector(earth.pos-craft.pos)
    magR=mag(earth.pos-craft.pos)
    craft.p= craft.M*vector(sqrt(3)/2,0.5,0)*sqrt(G*earth.M/magR)
    while t<=6400:
        rate(100)
      
        R=vector(earth.pos-craft.pos)
        magR=mag(earth.pos-craft.pos)
        force=G*earth.M*craft.M*R/magR**3
        craft.p=craft.p+force*dt
        craft.pos=craft.pos+(craft.p/craft.M)*dt
        t=t+dt
        craft.trail.append(pos=craft.pos)



##These three  while-loops execute the launch from orbit to moon.       

 
##initial conditions
while t>6400:
    while t <=56190:##t=56190 is the total duration to reach the moon.  
        ##print("time, " +str(t))
        Rce=earth.pos-craft.pos
        magRce=mag(Rce)
        Rcm=moon.pos-craft.pos
        magRcm=mag(Rcm)
        craft.pos=vector(-0.5*(50000+6.4e6+1.0e6),sqrt(3)*(50000+6.4e6+1.0e6)/2,0)##I had to remind python about the initial launch position of the craft because the position corresponding to t=6400 was slightly off the intended launch position.
        craft.p=craft.M*vector(0.875,0.4625,0)*1.3e4##The real direction of the tangent velocity to the position of the craft is (0.8660,0.5,0), difference of(0.009,-0.0375,0), but this direction did not give me the result I wanted.
        craft.trail=curve(pos=craft.pos,color=craft.color,radius=0.5*craft.radius)
        scene.autoscale=0

##calculations

        while t<=56190:
            rate(100)
            ##print("time, " +str(t))
            cm=magRcm-craft.radius-moon.radius
            Rce=earth.pos-craft.pos
            magRce=mag(Rce)
        
            Rcm=moon.pos-craft.pos
            magRcm=mag(Rcm)

            ##print("position " +str(craft.pos))
            ##print('distance to moon'+str(cm))

            eforce=G*earth.M*craft.M*Rce/magRce**3
            mforce=G*moon.M*craft.M*Rcm/magRcm**3
            force=eforce+mforce
    
            craft.p=craft.p+force*dt
            craft.pos=craft.pos+craft.p/craft.M*dt
    
            t=t+dt
            craft.trail.append(pos=craft.pos)
    
            Remag = mag(earth.pos-craft.pos) #distance craft to centre of earth
            Rmmag = mag(moon.pos-craft.pos) #distance craft to centre of moon

            if Remag<=earth.radius:
                print ("Oops, crashed in to earth!")

            if Rmmag<=moon.radius+craft.radius:##I thought that adding the craft's radius made more sense to indicate that the craft had made contact with the moon.
                print("Mission accomplished, crashed into Moon at time"+str(t))

