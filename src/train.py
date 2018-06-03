import os
import numpy as np
import nibabel as nib
import configparser
import json
from nilearn import plotting

# parse in config to see where to read the files in from
config = configparser.ConfigParser()
config.read('../config.ini')
location = config['FILES']['Location']
print(location)
