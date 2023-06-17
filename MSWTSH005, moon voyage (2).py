from vpython import *

                    ##objects

earth=sphere(pos=vector(0,0,0),radius=6.4e6,color=color.blue,opacity=1)
moon=sphere(pos=vector(4.0e8,0,0),radius=1.75e6,color=color.white)
craft=sphere(pos=vector(-0.5*(50000+6.4e6+1.0e6),sqrt(3)*(50000+6.4e6+1.0e6)/2,0),radius=1.0e6,color=color.red)
craft.trail=curve(pos=craft.pos,color=craft.color)
sun=sphere(pos=vector(-1.5e11,0,0),radius=1.5e10,color=color.yellow)##sun
                    ##constants
sun.M=2e30##sun
G=6.67e-11
earth.M=6.0e24
moon.M=7.0e22
craft.M=175.0
dt=10
t=0
work=0
dKineticEnergy=0
                    ## These two while-loops execute the one orbit around the earth.
while t<=6400:      ##t=6400 is the time after one orbit around the earth.
    R=vector(earth.pos-craft.pos)
    magR=mag(earth.pos-craft.pos)
    craft.p= craft.M*vector(sqrt(3)/2,0.5,0)*sqrt(G*earth.M/magR)
    ##sunearth
    R=vector(earth.pos-sun.pos)
    magR=mag(earth.pos-sun.pos)
    earth.p=earth.M*vector(0,sqrt(G*sun.M/magR**2),0)
    earth.trail=curve(pos=earth.pos,color=earth.color)
    scene.autoscale=0
    while t<=6400:
        rate(100)
        Rce=earth.pos-craft.pos
        magRce=mag(Rce)
        Rcm=moon.pos-craft.pos
        magRcm=mag(Rcm)
        eforce=G*earth.M*craft.M*Rce/magRce**3
        mforce=G*moon.M*craft.M*Rcm/magRcm**3
        force=eforce+mforce
        craft.p=craft.p+force*dt
        craft.pos=craft.pos+(craft.p/craft.M)*dt
        t=t+dt
        craft.trail.append(pos=craft.pos)
        ##sunearth
        R=vector(earth.pos-sun.pos)
        magR=mag(earth.pos-sun.pos)
        R=vector(earth.pos-sun.pos)
        sforce=-G*sun.M*earth.M*R/magR**3

        earth.p=earth.p+sforce*dt
        earth.pos=earth.pos+(earth.p/earth.M)*dt
        earth.trail.append(pos=earth.pos)
        scene.autoscale=0


                    ##These three following while-loops execute the launch from orbit to moon.


                    ##initial conditions.
while t>6400:
    while t <=56190:##t=56190 is the total duration to reach the moon.
        Rce=earth.pos-craft.pos
        magRce=mag(Rce)
        Rcm=moon.pos-craft.pos
        magRcm=mag(Rcm)
        craft.pos=vector(-0.5*(50000+6.4e6+1.0e6),sqrt(3)*(50000+6.4e6+1.0e6)/2,0)##I had to remind python about the initial launch position of the craft because the position corresponding to t=6400 was slightly off the intended launch position.
        craft.p=craft.M*vector(0.875,0.4625,0)*1.3e4##The real direction of the tangent velocity to the position of the craft is (0.8660,0.5,0), difference of(0.009,-0.0375,0), but this direction did not give me the result I wanted.
        craft.trail=curve(pos=craft.pos,color=craft.color,radius=0.5*craft.radius)
        scene.autoscale=0
        ##sunearth
        R=vector(earth.pos-sun.pos)
        magR=mag(earth.pos-sun.pos)
        earth.p=earth.M*vector(0,sqrt(G*sun.M/magR**2),0)
        earth.trail=curve(pos=earth.pos,color=earth.color)

                    ##calculations.

        while t<=56190:
            rate(100)
            Rce=earth.pos-craft.pos
            magRce=mag(Rce)
            Rcm=moon.pos-craft.pos
            magRcm=mag(Rcm)
            eforce=G*earth.M*craft.M*Rce/magRce**3
            mforce=G*moon.M*craft.M*Rcm/magRcm**3
            force=eforce+mforce
            deltap=force*dt
            ##sunearth
            R=vector(earth.pos-sun.pos)
            magR=mag(earth.pos-sun.pos)
            R=vector(earth.pos-sun.pos)
            sforce=-G*sun.M*earth.M*R/magR**3

            earth.p=earth.p+sforce*dt
            earth.pos=earth.pos+(earth.p/earth.M)*dt
            earth.trail.append(pos=earth.pos)


                    ##work calculation.
            deltar=(force*dt/craft.M)*dt
            w= dot(force,deltar)
            work=work+w
            magp=mag(craft.p)
                    ##################
            craft.p=craft.p+force*dt
                    ##change in kinetic energy calculation.
            deltap=force*dt
            magdeltap=mag(deltap)
            deltaK=0.5*craft.M*(magdeltap/craft.M)**2
            dKineticEnergy=dKineticEnergy+deltaK
                    ############################
            craft.pos=craft.pos+(craft.p/craft.M)*dt
            t=t+dt
            craft.trail.append(pos=craft.pos)
            scene.autoscale=0
            Remag = mag(earth.pos-craft.pos) #distance craft to centre of earth.
            Rmmag = mag(moon.pos-craft.pos) #distance center of craft to centre of moon.

            if Remag<=earth.radius:
                print ("Oops, crashed in to earth!")

            if Rmmag<=moon.radius+craft.radius:##I thought that adding the craft's radius made more sense to indicate that the craft had made contact with the moon.
                print('*******************************************************')
                print("Mission accomplished, crashed into Moon at time "+str(t)+" seconds")
                print("work= "+str(+work)+" Joules")
                print("dKinetic energy = "+str(dKineticEnergy)+" Joules")
                print('*******************************************************')
