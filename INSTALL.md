# MotionClouds: installing and running the python scripts

MotionClouds are parameterized stimuli with controlled motion content and no spatial coherence.  They are precisely tuned in the frequency space.

* A full description can be found in Paula S. Leon, Ivo Vanzetta, Guillaume S. Masson, Laurent U. Perrinet. Motion Clouds: Model-based stimulus synthesis of natural-like random textures for the study of motion perception, URL . Journal of Neurophysiology, 107(11):3217--3226, 2012, see  http://www.ncbi.nlm.nih.gov/pubmed/22423003 or http://jn.physiology.org/content/107/11/3217 .

## installing and running the python scripts
This package consists of:
* ```MotionClouds.py``` : the API with all the math and display routines,
* ```test_*.py``` : different types of stimuli are tested,
* ```experiment_*py``` : different experiments.
* ```fig_*py``` : different scripts used to generate wiki pages.
* ```figures``` : resulting figures of tests and experiments (as set in the variable ```MotionClouds.figpath```.
* ```Makefile``` : a GNUmake file to edit files ```make edit```, generate figures ```make figures``` or compile the documentation ```make doc```.

## Installation

*   MotionClouds consist of a one-file python script: Installation consists simply in downloading the ```MotionClouds.py``` file which contains all routines to compute and use the MotionClouds textures. This script uses python (http://python.org) which comes (pre-installed /  easy to download and install) on many operating systems.

* MotionClouds may easily be installed using

```
    pip install MotionClouds
```

* Other solutions consist to simply grab this file at: https://raw.githubusercontent.com/NeuralEnsemble/MotionClouds/master/MotionClouds.py and to use it along with the examples.

* Installation has some dependencies:
 1. mandatory: ```numpy``` is the core library used to compute textures,
 1. optional: ```mayavi``` is used to visualize envelopes,
 1. optional: ```ffmpeg``` is used to generate movies.
 1. optional: ```matplotlib```, ```scipy``` (with PIL support) and ```imagemagick``` are used to generate figures in the documentation.
 1. optional: ```progressbar``` for displaying progress of encoding.
 1. optional: ```texlive-latex-recommended  latexmk latexdiff``` to compile the documentation
 1. optional: ```PyOpenGL PyOpenGL_accelerate glumpy``` to display MotionClouds online

* These dependencies may  be easily met using the dedicated scripts:

 * For MacOsX, first install command line tools by typing the ```git``` command in the terminal (a pop-up message should happen if these tools are not installed). Then issue the following command in the terminal:
```
    curl https://raw.githubusercontent.com/NeuralEnsemble/MotionClouds/master/install/install_dependencies_macosx.sh |sh
```
 * For Debian-like systems, issue the following command in the terminal
```
    wget https://raw.githubusercontent.com/NeuralEnsemble/MotionClouds/master/install/install_dependencies_debian.sh -O - |sh
```

Again, these line of code may be copy-and-pasted in your terminal.


## download

* to get the latest version, download the current state from the repository:
```
git clone https://github.com/meduz/MotionClouds.git
```

* other sources exist to get a stable release, such as ModelDb (http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146953).

* This iinstallation procedure was tested on several MacOsX/Mavericks 64bit machines, Snow Leopard 10.6-32bits and on ubuntu 14.04 LTS / Debian squeezy 64bit machines.

##testing

* To test the basic functionality of Motion Clouds, try in the terminal:

```
python -c'import MotionClouds as mc; fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame); z = mc.envelope_gabor(fx, fy, ft)'
```

* If that fails, we will be happy to help out, so send an e-mail to laurent.perrinet@univ-amu.fr.
