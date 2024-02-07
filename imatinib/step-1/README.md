## Step 1 - ligand preparation

#### software needed [installation instructions](../../)

 - scrubber
 - meeko

### 1-a. Generate coordinates and protonation states


Run `scrub.py` on a terminal with the `autodock` micromamba environment active
to prepare imatinib from SMILES.

```
scrub.py "Cc1ccc(cc1Nc2nccc(n2)c3cccnc3)NC(=O)c4ccc(cc4)CN5CCN(CC5)C" -o imatinib.sdf
```
Note that three isomers were produced: three tautomer states in this case.
Let's visualize with Pymol by typing the following in the terminal:

```
pymol imatinib.sdf
```

Observations:
 - both amines are protonated, but at neutral pH, only one is protonated
 - there are three protonation states (use keyboard arrows, or arrows in bottom right corner)
 - one substituent in the piperazine is not equatorial

We won't be docking the full imatinib molecule. This is to illustrate
difficulties with ligand preparation.


### 1-b. Use part of imatinib

Use the `--skip_tautomers` option to stick to the tautomer state in the SMILES,
which is imatinib without the piperazine and the aromatic ring adjacent to it.

```
scrub.py "Cc1ccc(cc1Nc2nccc(n2)c3cccnc3)NC(=O)C" -o lig.sdf --skip_tautomers
```

Convert `lig.sdf` to PDBQT format, for autodock.
```
mk_prepare_ligand.py -i lig.sdf
```

The above wrote `lig.pdbqt`. It can be inspected with Pymol.



#### move on to [step-2](../step-2)

#### back to [step-0](../step-0)

#### [imatinib tutorial contents](../)
