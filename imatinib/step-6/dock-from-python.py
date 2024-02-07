#!/usr/bin/env python

from vina import Vina
from rdkit import Chem
from rdkit.Chem import AllChem
from meeko import MoleculePreparation
from meeko import PDBQTMolecule
from meeko import RDKitMolCreate
from scrubber import Scrub

# embed ligand
scrub = Scrub(ph_low=7.4, ph_high=7.4)
rdmol = Chem.MolFromSmiles("C1C(O)CC=CC=CCC=CC=CC(=O)CC(C(=O)O)C1")
isomers = scrub(rdmol)

# consider only the first protonation state
# each molecule may have more than one conformer
# meeko will consider only the first conformer, need to change meeko
mol = isomers[0]

# prepare ligand pdbqt
meeko_prep = MoleculePreparation()
meeko_prep.prepare(mol)
lig_pdbqt = meeko_prep.write_pdbqt_string()

# dock
v = Vina(sf_name='vina')
v.set_receptor("rec_2hzn.pdbqt")
v.set_ligand_from_string(lig_pdbqt)
v.compute_vina_maps(center=(15, 54, 17), box_size=(18, 27, 24))
v.dock()
output_pdbqt = v.poses(n_poses=5)

# convert to SDF and write
pmol = PDBQTMolecule(output_pdbqt)
output_rdmol_list = RDKitMolCreate.from_pdbqt_mol(pmol)
output_rdmol = output_rdmol_list[0] # side chains would be extra items in this list
f = Chem.SDWriter('docking-results-from-python.sdf')
for conf in output_rdmol.GetConformers():
    f.write(output_rdmol, confId=conf.GetId())
f.close()
