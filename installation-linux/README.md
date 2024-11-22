## Install micromamba

If you are already using conda or mamba, you can use that and skip this step.
Installation instructions are on
[micromamba's website](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html).
You can use micromamba alongside mamba or conda.

Installing it consists of running the following command, and following the
instructions displayed in the prompt. Pasting is Ctrl + shift + V.
```
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

After installation, typing `micromamba` should print the help message.



## Install dependencies with micromamba

This will install several packages from conda-forge, the default
channel in micromamba.

First, we create a new environment called "autodock", and activate it.
```
micromamba create -n autodock
micromamba activate autodock
```

Then we install the packages. Make sure the desired environment,
autodock, is active, by checking that the prompt starts with `(autodock)`.
If not, run `micromamba activate autodock`

```
micromamba install python=3.11 -y
micromamba install pymol-open-source -y
micromamba install rdkit numpy scipy -y
micromamba install chemicalite matplotlib=3.7 pandas multiprocess -y
```

Several packages are being installed in a single line.
We still used a few lines just to avoid a single very long line.

Now, running `python` should indicate version 3.11 packaged by conda-forge.
Inside the Python interpreter, `import rdkit` should raise no errors.
In the command line (after exiting the Python interpreter with Ctrl-D or `exit()`),
running `pymol` should launch the molecular viewer.



## Install Meeko and Ringtail from PyPI

Running the following commands will install meeko and ringtail in
the currently active micromamba environment.

```
pip install meeko==0.6.0a3
pip install ringtail
```

Running the following commands should display help messages:
```
mk_prepare_ligand.py
rt_process_vs.py
```

A new release of Meeko will be available soon.
Updating consists of running `pip install` again and pointing to the
desired version. Omitting the version defaults to the latest stable version.



## Install scrubber from GitHub

We haven't yet created a release for the scrubber package. Until then, it
needs to be installed by creating a copy of the source code.

First we navigate to where in the filesystem we want to create the copy,
using commands `cd` (change directory) and `mkdir` (make directory):

```
cd /home/myusername
mkdir autodock_code
cd autodock_code
```

Now, download the repository with `git clone`, which creates a new directory (folder) called
scrubber, then change directory into it, and install in the currently active
micromamba environment with `pip`:

```
git clone https://github.com/forlilab/scrubber.git
cd scrubber
pip install .
cd ..
```

The last command, `cd ..`, goes back one folder.
Running `scrub.py` should print the help message.



## Vina executable

The binary file is available under "Releases" on the right side of
[Vina's GitHub page](https://github.com/ccsb-scripps/AutoDock-Vina).
Here's a [direct link to the releases page](https://github.com/ccsb-scripps/AutoDock-Vina/releases).
The filename is `vina_1.2.5_linux_x86_64`.


Give the file permission to execute with `chmod`:
```
chmod +x vina_1.2.5_linux_x86_64
```

Executing the file should display the help message
```
./vina_1.2.5_linux_x86_64 
```



## Check that everything works with a toy example

Copy the files in [toy-example-data](../toy-example-data) to the working dir and run the following commands.

```
scrub.py "Oc1ccccc1" -o phenol.sdf
mk_prepare_ligand.py -i phenol.sdf -o phenol.pdbqt
mk_prepare_receptor.py --pdb pocket.pdb --ligand pocket.pdb --padding 5 -o receptor
mkdir results
./vina_1.2.5_linux_x86_64 --receptor receptor.pdbqt --config receptor.box.txt --ligand phenol.pdbqt --out results/phenol.pdbqt
rt_process_vs.py write -o results.db -fp results -m vina -ai -rf receptor.pdbqt
mkdir passing_sdf
rt_process_vs.py read -i results.db -e -2 -sdf passing_sdf
```

A file "phenol.sdf" should have been added to "passing\_sdf".
