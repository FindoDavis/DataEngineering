
"""Created on Wed Oct  9 07:49:12 2019
Purpose: Generate  a csv format file from a fixedwidth file
@author: Findo Davis
"""
import json
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "main.log",
                    level = logging.DEBUG,
                    format=LOG_FORMAT,
                    )
logger = logging.getLogger()

def generate_file (specfilename):
    logger.info ('createCSV_From_FixedWidthDat Batch Started ')
    try:
        with open (specfilename) as json_files:
            data = json.load(json_files) 
            logger.info("{} File read completed in job createCSV_From_FixedWidthDat".format(specfilename))
    except :
        logger.error("Cannot open the specified file ".format(specfilename))

    csv=open("csvFile.dat","w") 
    no_col=len(data["ColumnNames"])
    #Iterate through the fixed fidth file an load the csv file
    with open('fixedwidthFile.dat', 'r') as f:
        for line in f:
            fwl=line[2:-2]
            csvline=''
            pos=0
            for i in range(no_col):          
                csvfield=fwl[pos:pos+int(data["Offsets"][i])].rstrip()
                pos=pos+int(data["Offsets"][i])
                if i!=no_col-1:
                    csvline=csvline+csvfield+','
                else:
                    csvline=csvline+csvfield
            print(csvline.encode(data['DelimitedEncoding']),file=csv)
    csv.close()
    logger.info('createCSV_From_FixedWidthDat batch finished ' )

if __name__ == '__main__':
    generate_file('spec.json')
    
