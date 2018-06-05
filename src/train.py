import os
import numpy as np
import nibabel as nib
import configparser
import json
import csv
from nilearn import plotting
from enum import Enum, auto
import re



# parse in config to see where to read the files in from

DementiaStrings = ["AD dem/FLD prior to AD dem", 
                    "AD dem w/depresss  not contribut", 
                    "AD dem w/depresss- not contribut", 
                    "AD dem w/Frontal lobe/demt at onset", 
                    "Incipient demt PTP", 
                    "AD dem w/oth (list B) not contrib", 
                    "AD dem distrubed social- prior", 
                    "Vascular Demt  primary", 
                    "AD dem Language dysf with", 
                    "AD dem distrubed social- with", 
                    "DAT", 
                    "DLBD- secondary", 
                    "DAT w/depresss not contribut", 
                    "Frontotemporal demt. prim", 
                    "AD dem Language dysf after", 
                    "AD dem w/CVD not contrib", 
                    "AD dem w/oth unusual features", 
                    "AD dem w/PDI after AD dem not contrib", 
                    "AD dem w/oth (list B) contribut", 
                    "AD dem cannot be primary", 
                    "AD dem Language dysf prior", 
                    "AD dem visuospatial- prior", 
                    "AD dem w/oth unusual features/demt on", 
                    "AD dem w/depresss- contribut", 
                    "AD dem w/CVD contribut", 
                    "AD dem visuospatial- with", 
                    "DLBD- primary", 
                    "Incipient Non-AD dem", 
                    "Dementia/PD- primary", 
                    "AD dem distrubed social- after", 
                    "Vascular Demt- secondary", 
                    "AD dem w/depresss  contribut", 
                    "AD Dementia", 
                    "AD dem w/PDI after AD dem contribut", 
                    "AD dem w/oth unusual feat/subs demt", 
                    "Vascular Demt- primary",
                    "Dementia"]
NoDementiaStrings = ["ProAph w/o dement", 
                        "Non AD dem- Other primary", 
                        "Cognitively normal", 
                        "No dementia",
                        "NoDementia"]
class Dementia(Enum):
    DEMENTIA = "Dementia"
    NO_DEMENTIA = "No_Dementia"
    UNKNOWN = "Unknown"

    @staticmethod
    def from_str(string):
        if string in DementiaStrings:
            return Dementia.DEMENTIA
        elif string in NoDementiaStrings:
            return Dementia.NO_DEMENTIA
        print(string)
        return Dementia.UNKNOWN


patient_results = {}
with open('../patient_diagnosis_processed.csv') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        rowObj = {}
        for h, v in zip(headers, row):
            rowObj[h] = v
        if rowObj['Subject'] not in patient_results:
            patient_results[rowObj['Subject']] = []
        patient_results[rowObj['Subject']].append(rowObj)

patient_id_to_results = {}
for subject, subjectData in patient_results.items():
    for data in subjectData:
        if data['dx1'] is '':
            continue
        if subject not in patient_id_to_results:
            patient_id_to_results[subject] = [Dementia.from_str(data['dx1'])]
        else:
            patient_id_to_results[subject].append(Dementia.from_str(data['dx1']))


for subject, data in patient_id_to_results.items():
    if len(data) is 1:
        patient_id_to_results[subject] = data[0]
    elif len(data) > 1 and len(set(data)) != 1:
        if Dementia.DEMENTIA in data:
            patient_id_to_results[subject] = Dementia.DEMENTIA
        elif Dementia.NO_DEMENTIA in data:
            patient_id_to_results[subject] = Dementia.NO_DEMENTIA
        else:
            patient_id_to_results[subject] = Dementia.UNKNOWN
    else:
        patient_id_to_results[subject] = data[0]


config = configparser.ConfigParser()
config.read('../config.ini')
location = config['FILES']['Location']

# find all the files in the folder
raw_scan_ids = [x for x in os.listdir(location)]
if '.DS_Store' in raw_scan_ids: raw_scan_ids.remove('.DS_Store')

id_extractor_pattern = re.compile('(.*?)_')

labelled_scan_ids = []

for raw_scan_id in raw_scan_ids:
    m = id_extractor_pattern.match(raw_scan_id)
    scan_id = m.group(1)
    if scan_id not in patient_id_to_results:
        continue
    elif patient_id_to_results[scan_id] is Dementia.UNKNOWN:
        continue
    labelled_scan_ids.append((scan_id, raw_scan_id))

FLAG = "T1w" #or T2w
mri_extractor_pattern = re.compile('anat[0-9]*')

if FLAG is "T1w":
    mri_type_pattern = re.compile(".*T1w.nii.gz")
else:
    mri_type_pattern = re.compile(".*T2w.nii.gz")

paths = {}

for scan_id, raw_scan_id in labelled_scan_ids:
    raw_scan_id = location + "/" + raw_scan_id
    scans = [x for x in sorted(os.listdir(raw_scan_id)) if mri_extractor_pattern.match(x)]
    scanLocations = []
    for scan in scans:
        scan_folder = raw_scan_id + "/" + scan
        scanTypeMatch = [x for x in sorted(os.listdir(scan_folder)) if mri_type_pattern.match(x)]
        if scanTypeMatch:
            scanLocations.append(scan_folder + "/" + scanTypeMatch[0])
    if scan_id not in paths:
        paths[scan_id] = []
    paths[scan_id].append(scanLocations)
# print(paths)
    
# so the paths are ordered in a list like array, and idea is to take each index of list or
# each file and feed .nii file to sci kit learn somehow. 
# var c=10

path_string = ""

for personId, MRISession in paths.items():
    for MRI in sorted(MRISession):
        path_string = path_string + str(sorted(MRI)[0]) + " "
        

print(path_string)
