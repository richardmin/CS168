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

# find all the files in the folder
raw_scan_ids = [x for x in os.listdir(location)]

if '.DS_Store' in raw_scan_ids: raw_scan_ids.remove('.DS_Store')
