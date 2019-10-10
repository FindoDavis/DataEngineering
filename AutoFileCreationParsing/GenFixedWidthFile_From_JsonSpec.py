
"""
Created on Wed Oct  9 01:08:49 2019
Purpose: Generate  a fixed width file by using the specifications in spec file
@author: Findo Davis
"""

import json
import random
import string 
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "main.log",
                    level = logging.DEBUG,
                    format=LOG_FORMAT,
                    )
logger = logging.getLogger()

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate_file (specfilename):  
    logger.info (" GenFixedWidthFile_From_JsonSpec batch started ")   
    try:
        with open (specfilename) as json_files:
            data = json.load(json_files)
            logger.info ("{} File read completed in GenFixedWidthFile_From_JsonSpec".format(specfilename))   
    except :
        logger.error(" Could not open the specified file ".format(specfilename))
    no_col=len(data["ColumnNames"])

    for i in range(no_col):
        if len(data["ColumnNames"][i]) > int(data["Offsets"][i]):
            logger.error ("Column header length more than the offset")
    F = open("fixedwidthFile.dat","w") 

    #Generate fixedwidth Header
    if data["IncludeHeader"]=='True':
        line=''
        for i in range(no_col):
            if len(data["ColumnNames"][i]) <= int(data["Offsets"][i]):
                pad=int(data["Offsets"][i]) 
                line=line+data["ColumnNames"][i].ljust(pad)
                #print(line.encode('windows-1252'),end='',file=F)
        print(line.encode(data['FixedWidthEncoding']),file=F)       

    #Generate fixed with file with given set of rows
    for x in range(3):
        line=''
        for i in range(no_col):
            pad=int(data["Offsets"][i])
            line=line+randomString(int(data["Offsets"][i]))
        print(line.encode(data['FixedWidthEncoding']),file=F)   
    F.close()
    logger.info('GenFixedWidthFile_From_JsonSpec Batch Finished ')
if __name__ == '__main__':
    generate_file('spec.json')    
