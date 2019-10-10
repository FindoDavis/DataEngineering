
"""
Created on Wed Oct  9 23:49:21 2019
Purpose: 1.This script call in functions to generate fixedwidth file based on the 
         specification given in json file 
         2. A csv format file is also created from the fixedwidth file
@author: Findo Davis
"""
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "main.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

logger.info (" main batch started ")
from GenFixedWidthFile_From_JsonSpec import generate_file as fwdf
from createCSV_From_FixedWidthDat import generate_file as csvf
specfile='spec.json'
def __init__ (self,specfile):
    self.specfile=specfile
    
fwdf(specfile)
csvf(specfile)

logger.info (" main batch finished ")
