## Step 4 - launching the virtual screening

```
cp tutorials/imatinib/step-4/mols.smi .
scrub.py mols.smi -o mols.sdf

mkdir mols_pdbqt
mk_prepare_ligand.py -i mols.sdf --multimol_outdir mols_pdbqt
```

With autodock-gpu
```
mkdir vs_adgpu
/disk/diogom/code/AutoDock-GPU/bin/autodock_gpu_128wi -B mols_pdbqt/*.pdbqt -M rec_3oxz_rot315_rigid.maps.fld -F rec_3oxz_rot315_flex.pdbqt -N vs_adgpu -C 1
```

Or With vina
```
mkdir vs_vina
./vina_1.2.5_linux_x86_64 --scoring ad4 --maps rec_3oxz_rot315_rigid --flex rec_3oxz_rot315_flex.pdbqt --batch mols_pdbqt/*.pdbqt --dir vs_vina/
```

Use ringtail script to assemble results into sqlite database file
```
rt_process_vs write -o vs_adgpu.db -fp mols_pdbqt/vs_adgpu*
```

With vina, we tell it to add interactions (`-ai`) with the receptor file (`-rf`)
```
rt_process_vs write -o vs_vina.db -fp vs_vina/ -m vina -ai -rf rec_3oxz_rot315_rigid.pdbqt
```

For the next step, we will use a `.db` file that contains AutoDock-GPU results.

#### move on to [step-5](../step-5)

#### back to [step-3](../step-3)

#### [imatinib tutorial contents](../)
