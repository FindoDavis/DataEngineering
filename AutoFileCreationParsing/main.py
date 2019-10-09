
"""
Created on Wed Oct  9 23:49:21 2019

@author: jbksmaker
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
    
#ef main(self):
fwdf(specfile)
csvf(specfile)

logger.info (" main batch started ")
