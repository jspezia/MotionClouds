#!/usr/bin/env python
"""

Testing all possible export types 

"""


import MotionClouds as mc

name = 'export'

fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame)
color = mc.envelope_color(fx, fy, ft)

name_ = mc.figpath + name
z = mc.rectif(mc.random_cloud(color * mc.envelope_donut(fx,fy,ft)))

mc.anim_save(z, name_, display=False, vext='.mpg')
mc.anim_save(z, name_, display=False, vext='.zip')
mc.anim_save(z, name_, display=False, vext='.mat')
mc.anim_save(z, name_, display=False, vext='.h5')