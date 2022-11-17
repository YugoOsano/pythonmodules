# transcribed from
# https://github.com/libAtoms/GAP/blob/main/doc_src/gap_fitting_tutorial.ipynb
#  commands to run are:
#  $ python3 gap_fit_tutorial_runMD.py
#  $ gap_fit energy_parameter_name=energy force_parameter_name=forces do_copy_at_file=F sparse_separate_file=T gp_file=GAP.xml at_file=train.xyz default_sigma={0.008 0.04 0 0} gap={distance_2b cutoff=4.0 covariance_type=ard_se delta=0.5 theta_uniform=1.0 sparse_method=uniform add_species=T n_sparse=10}
#  $ quip E=T F=T atoms_filename=train.xyz param_filename=GAP.xml | grep AT | sed 's/AT//' > quip_train.xyz
#  $ quip E=T F=T atoms_filename=validate.xyz param_filename=GAP.xml | grep AT | sed 's/AT//' > quip_validate.xyz
#  $ python3 gap_fit_tutorial_plot.py

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy as cp
import ase.io
from ase import Atoms, Atom
from ase import units
from ase.build import molecule
from ase.md.langevin import Langevin
from ase.io.trajectory import Trajectory
def make_water(density, super_cell=[3, 3, 3]):
    """ Geenrates a supercell of water molecules with a desired density.
        Density in g/cm^3!!!"""
    h2o = molecule('H2O')
    # cbrt is cube root (of an array)
    a = np.cbrt((sum(h2o.get_masses()) * units.m ** 3 * 1E-6 ) / (density * units.mol))
    h2o.set_cell((a, a, a))         # https://wiki.fysik.dtu.dk/ase/ase/atoms.html#ase.Atoms.set_cell
    h2o.set_pbc((True, True, True)) # periodic boundary condition
    #return cp(h2o.repeat(super_cell))
    return h2o.repeat(super_cell)

from ase.calculators.emt import EMT
calc = EMT()
T = 150
water = make_water(1.0, [3,3,3])
water.set_calculator(calc)
dyn = Langevin(water, 1 * units.fs, T * units.kB, 0.0002)
def printenergy(a=water):
    epot = a.get_potential_energy() / len(a)
    ekin = a.get_kinetic_energy() / len(a)
    print('Energy per atom: Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  '
    'Etot = %.3feV' % (epot, ekin, ekin / (1.5 * units.kB), epot + ekin))
dyn.attach(printenergy, interval=5)
traj = Trajectory('dyn_emt.traj', 'w', water)
dyn.attach(traj.write, interval=5)
printenergy(water)
dyn.run(600)
out_traj = ase.io.read('dyn_emt.traj', ':')
for at in out_traj:
    at.wrap()
    if 'momenta' in at.arrays: del at.arrays['momenta']
ase.io.write('dyn_emt.xyz', out_traj, 'xyz')
isolated_H = Atoms('H', calculator=EMT(), cell=[20, 20, 20], pbc=True)
isolated_O = Atoms('O', calculator=EMT(), cell=[20, 20, 20], pbc=True)
print('e0_H:',isolated_H.get_potential_energy())
print('e0_O:',isolated_O.get_potential_energy())
ase.io.write('train.xyz', out_traj[0::2] + [isolated_H] + [isolated_O])
ase.io.write('validate.xyz', out_traj[1::2])
out_traj[0].arrays.keys()

#ase.io.write('image.png', water)

# the following files will be created after running this script
# validate.xyz, train.xyz, dyn_emt.xyz, dyn_emt.traj

#! gap_fit energy_parameter_name=energy force_parameter_name=forces do_copy_at_file=F sparse_separate_file=T gp_file=GAP.xml at_file=train.xyz default_sigma={0.008 0.04 0 0} gap={distance_2b cutoff=4.0 covariance_type=ard_se delta=0.5 theta_uniform=1.0 sparse_method=uniform add_species=T n_sparse=10}
# GAP.xml with intermediate files will be created by gap_fit command

# quip command is used to evaluate energies and forces with gained GAP params
# https://libatoms.github.io/QUIP/Tutorials/CCP5-June-2021.html#Standalone-QUIP-usage
#! quip E=T F=T atoms_filename=train.xyz param_filename=GAP.xml | grep AT | sed 's/AT//' > quip_train.xyz
#! quip E=T F=T atoms_filename=validate.xyz param_filename=GAP.xml | grep AT | sed 's/AT//' > quip_validate.xyz
