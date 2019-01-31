code test for kogan

to set up the code for this code test, do the following:

either clone this repo, or extract the tarball to a local directory.

Ensure python3 is installed  (python 3.6.5 was used to develop this)

bash $> which python3

should return a string like /usr/bin/python3, /usr/local/bin/python3, etc.
If not, install python3

create a python3 venv

bash $> python3 -m venv /dir/where/you/want/venv/installed


activate the venv

bash $> source /dir/where/you/want/venv/installed/bin/activate


inside the source directory that this file you are reading is in,
now you can install the python code requirements


bash $> pip3 install -r requirements.txt


and now run the code

bash $> python3 main.py
