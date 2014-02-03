List of things to improve in the code
=====================================

(by order of priority)

* make a class out of the `MotionClouds.py` library
* experiment_concentric.py : use a trick (forcing the phase) to generate concentric waves -> extend to experimentally show Kelvin's wake waves
* make a warning when the choice of parameter is not completley sane (for instance f_0 or B_sf greater than the Nyquist frequency of 0.5)
* use a Laplace (in itme) - Fourier (in space) transform to generate Motion Clouds as a stream of frames instead of the whole memory (would be good for memory concerns)
* DONE: use glumpy for displaying the movie online : fullscreen