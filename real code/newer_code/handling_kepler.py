import shutil
import os
import glob
from lightkurve import search_targetpixelfile
from astropy.io import fits
from astropy.table import Table
import matplotlib.pyplot as plt

def batch_download(starting_planet, ending_planet, mission):
    """Query to obtain FITS files corresponding to a confirmed exoplanet 
    from the Kepler or K2 missions. Sample usage might go like
    batch_download(1,3,"Kepler") to get FITS files for Kepler-1, 
    Kepler-2, and Kepler-3."""
    for identifier in range(int(starting_planet), int(ending_planet) + 1):
        tpf_collection = search_targetpixelfile(str(mission) +"-" + str(identifier), mission = mission).download_all()
def file_pusher(source_dir, target_dir):
    """Batch download downloads locally. If you want to move the
    FITS files to the current working directory, use_file_pusher.
    Input the path to the directory where the files originally are, 
    and then input the path to the directory where the files need to be."""
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

list_of_fits_files = []
for directory in os.listdir(os.path.join(os.getcwd(), "mastDownload/Kepler")):
    for filename in os.listdir((os.path.join(os.getcwd(), "mastDownload/Kepler", directory))):
        list_of_fits_files.append(filename)
        
# The above code generates a list of ALL the FITS files that 
# are within the current working directory.
    
unique_identifiers = []    
for filename in list_of_fits_files:
    if filename[0:13] not in unique_identifiers:
        unique_identifiers.append(filename[0:13])
        
# The above code generates a list of unique identifiers
# for the FITS files in the current working directory.
# It consists of the first twelve characters of the filename
# e.g. kplr0106659, which is the ID corresponding to each
# exoplanet. The length of the unique identifiers list
# will be equal to the number of exoplanets for which
# there are FITS files.
        
list_of_lists_of_filenames = [[] for x in range(len(unique_identifiers))]
for filename in list_of_fits_files:
    for i in range(len(unique_identifiers)):
        if filename[0:13] == unique_identifiers[i]:
            list_of_lists_of_filenames[i].append(filename)
        
# The above code separates the list of all the FITS files
# in the current working directory into a list of lists
# based on the parent directory e.g. to which star they belong.

for index in range(len(list_of_lists_of_filenames)):
    for index_2 in range(len(list_of_lists_of_filenames[index])):
        list_of_lists_of_filenames[index][index_2] = os.path.join(os.getcwd(), "mastDownload/Kepler", filename)
        
# The above code replaces filenames with filepaths for
# every filename in list_of_lists_of_filenames.
