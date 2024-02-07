## Python scripting

Our pip installation of Python binding for vina requires an older
version of python, 3.9. While this is not fixed, we can downgrade
python, and re-install meeko, scrubber, and ringtail.

```
micromamba install python=3.9
pip install vina
pip install meeko==0.6.0a3
pip install ringtail
cd scrubber
pip install .
```

Then run the example script:

```
cp tutorials/imatinib/step-6/dock-from-python.py .
python dock-from-python.py
```


#### back to [step-5](../step-5)

#### [imatinib tutorial contents](../)
