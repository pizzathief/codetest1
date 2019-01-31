code test for kogan

to set up the code for this code test, do the following:

either clone this repo, or extract the tarball to a local directory.

Ensure python3 is installed  (python 3.6.5 was used to develop this)
---------------------
which python3
---------------------
should return a string like /usr/bin/python3, /usr/local/bin/python3, etc.
If not, install python3

create a python3 venv
---------------------
python3 -m venv /dir/where/you/want/venv/installed
---------------------

activate the venv
---------------------
source /dir/where/you/want/venv/installed/bin/activate
---------------------

inside the source directory that this file you are reading is in,
now you can install the python code requirements

---------------------
pip3 install -r requirements.txt
---------------------

and now run the code
---------------------
python3 main.py
---------------------