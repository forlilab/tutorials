## Install Homebrew and Xcode Command Line Tools

Homebrew is arguably the most popular package manager for MacOS.
Installing it also installs Xcode Command Line Tools.
While we don't know for sure that Xcode Command Line Tools is strictly needed,
we didn't test an installation withtout it, and either Homebrew or Xcode Command
Line Tools may be useful in the future.

The official instructions are on [Homebrew's web page](https://brew.sh/). They consist of
running the following command in the terminal, and following the displayed instructions.
Since it downloads Xcode Command Line Tools (100 MB), it may take a
few minutes depending on the speed of the internet connection.

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

At the end of the installation, tt will print a couple of commands
to run in the terminal. Their purpose is to  make the command `brew` available
in the terminal. At that point, typing `brew` should display the help message.



## Install micromamba

If you are already using conda or mamba, you can use that and skip this step.
Installation instructions are on
[micromamba's website](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html).
You can use micromamba alongside mamba or conda.

Installing it consists of running the following command, and following the
instructions displayed in the prompt.
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
micromamba install python=3.11
micromambe install pymol-open-source
micromamba install rdkit numpy scipy
micromamba install chemicalite matplotlib pandas
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
The filename is `vina_1.2.5_mac_x86_64`.


Give the file permission to execute with `chmod` and remove quarantine with `xattr`:

```
chmod +x vina_1.2.5_mac_x86_64
xattr -d com.apple.quarantine vina_1.2.5_mac_x86_64
```

Executing the file should display the help message
```
./vina_1.2.5_mac_x86_64 
```

This binary file was compiled for Intel chips, but it is possible to run it
on Apple Silicon if Rosetta is installed. The following error indicates the
need to install Rosetta:

```
zsh: bad CPU type in executable: ./vina_1.2.5_mac_x86_64
```

To install Rosetta, you can enable it for Safari, and open or restart Safari to have
your Mac install Rosetta. To enable it for Safari, go to Apps in Finder,
right click Safari, open the Get Info dialog, and check the "Open using Rosetta" box.
More info: https://support.apple.com/en-us/HT211861#needsrosetta



## Check that everything works with a toy example

Copy the files in [toy-example-data](../toy-example-data) to the working dir and run the following commands.

```
scrub.py "Oc1ccccc1" -o phenol.sdf
mk_prepare_ligand.py -i phenol.sdf -o phenol.pdbqt
mk_prepare_receptor.py --pdb pocket.pdb --skip_gpf -o receptor
mkdir results
./vina_1.2.5_mac_x86_64 --receptor receptor.pdbqt --config receptor.box.txt --ligand phenol.pdbqt --out results/phenol.pdbqt
rt_process_vs.py write -o results.db -fp results -m vina -ai -rf receptor.pdbqt
mkdir passing_sdf
rt_process_vs.py read -i results.db -e -2 -sdf passing_sdf
```

A file "phenol.sdf" should have been added to "passing\_sdf".
