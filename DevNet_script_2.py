# ThreatGrid DevNet Learning Lab Lesson 3 Part 2
# This script will take a SampleID and obtain the
# associated analysis.json file from ThreatGrid

import requests
import json

tg_api_key = '<tg_api_key>'
sample_id = '<sample_id>'
filename = (sample_id + '.json')

# This function will write the returned data to a file
def write_to_file(analysis_file, filename):
    out_file = open(filename, 'w')
    out_file.write(json.dumps(analysis_file))
    out_file.close()

# This function will pull analysis.json data using the sampleID
def lookup_sampleID(sample_id, tg_api_key):
    url = 'https://panacea.threatgrid.com/api/v2/samples/{}/analysis.json?api_key={}'.format(sample_id, tg_api_key)
    request = requests.get(url).json()
    return request

########################
# Main calls start here
########################

# First we will retrieve the data from threatgrid by calling the lookup function
analysis_file = lookup_sampleID(sample_id, tg_api_key)

# Lets write the analysis file to disk for evaluation
write_to_file(analysis_file, filename)
