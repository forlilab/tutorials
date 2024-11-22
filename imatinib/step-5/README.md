## Step 5 - visually inspecting the virtual screening

We will use a `.db` file with results from autodock-gpu.
The imitanib part is included in the results. In this step
we will explore options that allow us to recover imatinib.

First let's look at the distribution of score and ligand efficiency
(score diveded by number of non-hydrogen atoms).
```
rt_process_vs read -i vs_adgpu.db --plot
```
This creates a file named "scatter.png".
It can be visualized using a file browser.

### 5a. visual inspection

```
mkdir passed
rt_process_vs read -i vs_adgpu.db -e -11 -sdf passed/
pymol tutorials/imatinib/step-2/2hzn_A.pdb rec_3oxz_rigid.pdbqt xray-imatinib.pdb passed/vs_adgpu_passing_results.sdf 
```

The carbamide of ZINC..309 resembles that of the ligand in PDB ID `2hzn`.

ZINC..429 illustrates the need for visual inspection:
 - two amides H-bonding nothing
 - elec clash with Glu286
 - void near Ile313
 - amide and benzene out of plane (no torsion potentials)

Note the void of imatinib near Lys271 without the two water molecules.
Showing mesh for the protein, and spheres for the small molecules,
with the show button (S in A/S/H/L/C on the right side of pymol),
helps visualzing shape complementarity.

If visually inspecting imatinib's binding mode without knowing that it is
a ligand, Would you rule out imatinib because of the void?


### 5b. filtering by energy and ligand efficiency


```
rt_process_vs read -i vs_adgpu.db -e -10
```

By opening the file "output\_log.txt", or running `tail output_log.txt`,
we that 42 ligands pass (out of ~500, so ~8%) and `lig` is included.
If we assume that most of the molecules are inactive, This is a poor hit rate.


We can see where imatinib is with respect to the other molecules.
```
rt_process_vs read -i vs_adgpu.db --plot -n lig
```
This creates a file called "scatter.png", in which each dot is a molecule,
the molecules in red are the ones that passed the filter (named "lig" in this case),
and the x and y axis are docking score and ligand efficiency.

If you get an error, try downgrading matplotlib:
```
micromamba install matplotlib=3.7
```

We can also filter by ligand efficiency, which is the docking score divided by
the number of non-hydrogen atoms. Run `rm passed/*.sdf` to delete the files
passed in the previous round (`rm` is to remove files).

```
rm passed/*.sdf
rt_process_vs.py read -i vs_adgpu.db --plot -le -0.33 -sdf passed/
pymol passed/*.sdf
```


### 5c. Filtering by interactions

Here's an example that returns poses with several contacts with the receptor.
The `-hb` flag is for H-bonds, and `-vdW` is for contacts in general.
```
rm passed/*.sdf
rt_process_vs.py read -i vs_adgpu.db --plot -hb "A:THR:315:" -hb "A:GLU:286:" -hb "A:ASP:381:" -vdw "A:ILE:313:" -hb "A:MET:318: -sdf passed/"
```

#### move on to [step-6](../step-6)

#### back to [step-4](../step-4)

#### [imatinib tutorial contents](../)
