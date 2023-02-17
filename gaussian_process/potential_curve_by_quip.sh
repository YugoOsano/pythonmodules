#!/usr/bin/bash
# ./potential_curve_by_quip.sh 2>/dev/null
# need GAP xml file sets in the working directory to run

xfix=20
rcutoff=5
dx=0.01
nstep=470
potentialrcutoff=0.0

for i in $( eval echo {0..$nstep} )
do
    x=`echo "$xfix+$rcutoff-$i*$dx" | bc -l`
    echo "2" > tmp.xyz
    echo "Lattice=\"40.0 0.0 0.0 0.0 40.0 0.0 0.0 0.0 40.0\" Properties=species:S:1:pos:R:3 Time=0.0" >> tmp.xyz
    echo "Si        $xfix      20.00000000      20.00000000" >> tmp.xyz
    echo "Si        $x      20.00000000      20.00000000" >> tmp.xyz
    #cat tmp.xyz

    # take -320.08028759756911 from
    # AT Time=0.00000000 energy=-320.08028759756911 cutoff=.....
    energy=`quip E=T F=T atoms_filename=tmp.xyz param_filename=gp_iter6_sparse9k.xml | grep 'energy=' | awk '{print $3}' | awk -F'=' '{print $2}'`
    distance=`echo "$x-$xfix" | bc -l`
    echo "$distance $energy"
done


