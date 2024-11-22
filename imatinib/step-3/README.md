## Step 3 - modeling the receptor to successfully dock imatinib

We will use imatinib's experimental pose to inform the selection.
This is not possible in a prospective screen, but helps us get a
sense of how modeling choices affect the results.

Since our search algorithms are stochastic, results vary occasionally.


### software needed

Go to [installation](../../) if needed

 - pymol (suffices to inspect results in folder "expected-results")
 - meeko
 - vina
 - autogrid (optionally)
 - autodock-gpu (optionally)



### 3a. docking to PDB ID `2hzn`

PDB ID `2hzn` which differs the most from `1iep` with
respect to the carboxylate oxygens of Glu286. PDB ID `1iep` was
crystallized with imatinib.

Copy the protein structure (no water, no ligand, hence the `_protein` suffix),
to the working directory:
```
cp tutorials/imatinib/step-3/2hzn_protein.pdb .
```

Also copy the x-ray imatinib from PDB ID `1iep` and the
molecule to dock (part of imatinib) if not already present in the
working directory from step 1:
```
cp tutorials/imatinib/step-3/xray-imatinib.pdb .
cp tutorials/imatinib/step-3/lig.pdbqt .
```

Convert to PDBQT with meeko:
```
mk_prepare_receptor.py -i 2hzn_protein.pdb -o rec_2hzn -p -v --padding 5 --box_enveloping xray-imatinib.pdb --allow_bad_res
```

It throws an error message because some residues have missing atoms.
With a "hope for the best" mindset, we will repeat the command but add `--allow_bad_res`.
Tip: the up-arrow brings up the last command.

Let's rename two of the files it wrote, with command `mv`:

```
mv rec_2hzn.box.pdb box.pdb
mv rec_2hzn.box.txt box.txt 
```

The `mv` command can be dangerous as the first filename is erased and the second is overwritten.

Visualize the search space:
```
pymol rec_2hzn.pdbqt xray-imatinib.pdb box.pdb
```
And type `as licorice, box` in pymol to properly display the search space.


Now, let's dock it with vina.

```
mkdir docked
./vina_1.2.5_linux_x86_64 --ligand lig.pdbqt --receptor rec_2hzn.pdbqt --config box.txt --out docked/2hzn.pdbqt
mk_export.py docked/2hzn.pdbqt
```

Replace `linux` by `mac` in `./vina_1.2.4_linux_x86_64` if using a mac.

Inspect whether or not any of the poses reproduces the binding mode of the amide.
Navigate poses with keyboard arrows, or by clicking the arrows on the right bottom corner.
```
pymol rec_2hzn.pdbqt xray-imatinib.pdb docked/2hzn_docked.sdf
```

The expected result is that neither of the poses reproduces the binding mode of the amide.
If any does, it's probably not one of the top poses.


### 3b. docking to PDB ID `3oxz` and with a flexible sidechain

PDB ID `3oxz` is more similar to `1iep` than `2hzn`.

Note `-p` alone to only generate the PDBQT file, and `-f "A:PHE:382"`,
to make Phe382 flexible. Two receptor PDBQT files are written as a result, one suffixed
with "\_rigid" for static atoms, and another with "\_flex" for movable atoms.

```
cp tutorials/imatinib/step-3/3oxz_protein.pdb .
mk_prepare_receptor.py -i 3oxz_protein.pdb -o rec_3oxz -p --allow_bad_res -f "A:382"
```

Dock with vina. Note the `--flex` option.

```
vina_1.2.5_linux_x86_64 --ligand lig.pdbqt --receptor rec_3oxz_rigid.pdbqt --flex rec_3oxz_flex.pdbqt --config box.txt --out docked/3oxz.pdbqt
mk_export.py docked/3oxz.pdbqt
```

### 3c. Which of the following are true?

We get the amide properly docked, in one of the top poses, because:
 - we used 3oxz
 - Phe 382 was flexible
 - does it really matter

These are questions one would ask while deciding which structure(s) to use for virtual screening.


### 3d. docking with the AD4 scoring function

Probably due to directional H-bonding terms, using the AD4 scoring function is
needed to produce a proper orientation of the aniline.

Let's make sure the hydroxyl of Thr 315 is properly oriented.
```
pymol 3oxz_protein.pdb
```

and in the command line of pymol:
```
show sticks
orient i. 315
h_add i. 315
```

Then:
1. click on the label button (`L` in A/S/H/L/C), then residues.
2. toggle to "3-Button Editing" by clicking on "Mouse Mode" (in green) on the bottom right corner
3. while pressing "Ctrl" on the keyboard, use the right mouse button to click on the
carbon-oxygen bond of Thr315, and drag to rotate the hydroxyl. Be sure to click closer
to the oxygen than to the carbon, to rotate the hydroxyl and not the protein. If you
accidentally rotate the protein, press `Ctrl` and `Z` to undo.
4. make sure the hydrogen is towards to the backbone carbonyl of Glu318.

Save the structure by entering the following in pymol's command line:
```
save 3oxz_rot315.pdb, 3oxz_protein
```

Make PDBQTs for this structure:
```
mk_prepare_receptor.py -i 3oxz_rot315.pdb -f "A:382" -o rec_3oxz_rot315 -p -g --box_enveloping xray-imatinib.pdb --padding 5 --allow_bad_res
```

Run autogrid to make AD4 maps
```
./tutorials/executables/autogrid4_linux -p rec_3oxz_rot315_rigid.gpf -l rec_3oxz_rot315_rigid.glg
```

Give permissions if needed. The `xattr` is only for Macs.
```
xattr -d com.apple.quarantine tutorials/executables/autogrid4_mac
chmod +x tutorials/executables/autogrid4_mac
```

If `autogrid4` didn't run, use the maps incuded in this repository,
by passing `--maps tutorials/imatinib/step-3/autogrid_maps/rec_3oxz_rot315_rigid`
to vina, instead of `--maps rec_3oxz_rot315_rigid`.

Dock with vina
```
./vina_1.2.5_linux_x86_64 --maps rec_3oxz_rot315_rigid --scoring ad4 --ligand lig.pdbqt --flex rec_3oxz_rot315_flex.pdbqt --out docked/3oxz_ad4.pdbqt
```

Or with AutoDock-GPU
```
./tutorials/executables/autodock_gpu_mac -M rec_3oxz_rot315_rigid.maps.fld -L lig.pdbqt -F rec_3oxz_rot315_flex.pdbqt -N docked/3oxz_ad4
mk_export.py docked/3oxz_ad4.dlg -c
```

Inspect with pymol

```
pymol rec_3oxz_rot315_rigid.pdbqt xray-imatinib.pdb docked/3oxz_ad4_docked.sdf
```


#### move on to [step-4](../step-4)

#### back to [step-2](../step-2)

#### [imatinib tutorial contents](../)
