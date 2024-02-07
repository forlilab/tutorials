## Step 0 - cloning this repository, command line basics

We will copy this repository with `git` and learn fundamental command line usage.


### 0-a. Clone the tutorials repository

In the terminal, navigate to the Desktop:

```
cd Desktop
```
`cd` stands for "chage directory". Create a folder named `autodock-bhive`
and change dir into it with two separate commands (type enter after each):

```
mkdir autodock-bhive
cd autodock-bhive
```

Clone the repository from github:
```
git clone https://github.com/forlilab/tutorials.git
```

### 0-b. basic commands in the terminal

Cloning the repository created a folder named "tutorials" in the Desktop.
You can inspect its contents with a file browser or within the terminal:

```
pwd
ls tutorials
cd tutorials
pwd
ls
ls imatinib
ls imatinib/step-1
cd ..
pwd
```

 - `pwd` print working directory
 - `ls` show files
 - `cd` change directory
 - `..` parent directory
 - `.` current directory

Use the `Tab` key to autocomplete. Instead of typing
`cd tutorials`, type `cd tut` and press `Tab`.

Copy and pasting is `Ctrl + shift + C` and `Ctrl + shift + V`.

`Ctrl + C` kills a running process.


### 0-c. get ready for step 1

Make sure we are in the right folder, `pwd` should return:
```
/home/your_username/autodock-bhive
```
where `your_username` is your actual username.

Copy the PDB file of the x-ray coordinates from the tutorials folder
```
cp tutorials/imatinib/step-1/xray-imatinib.pdb .
```
`cp` is to copy. The second argument is `.`, the current directory.

`cp` can delete data, for example, `cp file1 file2` would
delete the contents of `file2` if it already exists, by overwritting
`file2` with the contents of `file1`.

The `autodock` micromamba (or conda) environment should be active. If not, then
```
micromamba activate autodock
```
Then, `(autodock)` is displayed at the left of the terminal prompt.



#### move on to [step-1](../step-1)

#### [imatinib tutorial contents](../)
