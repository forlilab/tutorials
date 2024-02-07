## Step 2 - analysis of receptor conformations from the PDB

#### software needed [installation instructions](../../)

 - pymol

### 2-a. load proteins into pymol

No need for copying the files to current directory.
The \* is a wildcard and all seven PDB entries will be loaded.

```
pymol tutorials/imatinib/step-2/*.pdb
```

Strcutures are already aligned to each other and only the first chain
is present. Even though the assymetric unit is a dimer in some PDB entries,
the biological "assembly" is a monomer.


### 2-b. major loop change opens and closes pocket

In PDB IDs 1m52, 2qoh, and 3kf4, the pocket is occupied by the flexible loop.

Note how Phe382 in 1m52 clashes with imatinib in 1iep:

1. disable all objects except `1iep` and `1m52` by clicking on them on the right-side panel
2. type `show lines` in pymol command line
3. type `center i. 382` in pymol command line
4. scroll down (mouse/touchpad) to focus depth of viewer and improve visibility
5. on the righ-side panel, for the `all` object, click on the label button (`L` in A/S/H/L/C), 
and then "residues"
6. toggle `1m52` on and off to make the Phe382-imatinib clash clear

Based on this clash, we exclude 1m52, 2qoh, and 3kf4 as they are not able to accomodate imatinib.


### 2-c. inspect pocket around the amide

1. center on the amide oxygen of imatinib, by clicking on it with the middle mouse button
2. toggle to "3-Button Editing", by clicking on `Mouse mode` (in green) at the bottom right corner
3. pick the amide oxygen of imatinib by clicking on it, and then the backbone N of Asp381
4. type `dist` on the pymol command line. This creates a "distance" object for the picked atoms.
5. click on the background to unpick the picked atoms
6. repeat the above for imatinib's amide N and the closest carboxylate oxygen of Glu 286
8. toggle 3kfa, 2hzn, and 3oxz back on.

Inspect the nearby residues and try to guess how different the residues' coformation can
deviate from `1iep` to enable successful docking of imatinib. In particular, which structures
are good enough to reproduce the H-bonds of imatinib's amide.



### 2-d. inspect pocket around the aminopyrimidine

1. toggle off `2hzn`, `3kfa`, and `3oxz`
2. center on imatinib's aniline nitrogen
3. draw the H-bond between the aniline nitrogen and the hydroxyl of Thr315
4. center of Phe382
5. toggle `2hzn`, `3kfa`, and `3oxz` back on

The loop containing Tyr 253 is very flexible. There's no good way to model this in docking.

Note the two-water network between imatinib's pyrimidine and Glu 286. Would you keep any of these
waters for virtual screening?

Flexible parts of the protein show variability across structures.
Some of these conformations have a clash between Phe382 and imatinib.

The B-factors are another way to infer local protein flexibility. Toggle all structures off
except `1iep`, click on the color button for `1iep` (`C` in A/S/H/L/C), spectrum, b-factors.
Warmer colors are generally associated with more flexible parts. Do not do this for the `all`
object, as B-factor differences across structures are not as informative about protein
flexibility as relative differences within the same structure.



### How would you model the receptor for virtual screening?

 - keep waters?
 - flexible sidechains? which ones? (backbone always rigid in autodock)
 - multiple conformations? how many?



#### move on to [step-3](../step-3)

#### back to [step-1](../step-1)

#### [imatinib tutorial contents](../)
