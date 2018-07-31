# ThreatGrid Basic API Library
# Author: Jesse Munos
# Date: July 2018
# Description: This script takes a sampleID or a sha256 and reaches out to
# ThreatGrid to pull the analysis.json file

# Lets declare our imports we will use argv to take in the sampleID or SHA256
# We will use re for regex match checking
from sys import argv
import requests
import re
import json

# Grab the input from CLI execution
script, sample_identifier, api_key, filename = argv

# Lets just tell the user what values were provided
def talk_to_user(script, sample_identifier, api_key):
    print(f"You are running the {script} script.")
    print("Inputs are in the following order: <sample_identifer> <(SHA256 or SampleID)> and <API key>")
    print(f"The format is: {script} sample_identifer API_key")
    print(f"You provided the following sample_identifier: {sample_identifier}")
    print(f"You provided the following API_Key: {api_key}")

# Setup regular expresion checks to determine what
# type of data the user provided
def is_sha256(sample_identifier):
    return bool(re.match(r'^[A-Fa-f0-9]{64}$', sample_identifier))

def is_sampleID(sample_identifier):
    return bool(re.match(r'^[A-Fa-f0-9]{32}$', sample_identifier))

# We will define some methods here for interacting with the system.
# This fucntion will pull the summary data using the SHA256
def lookup_sha(sample_identifier, api_key):
    url = 'https://panacea.threatgrid.com/api/v2/search/submissions?q={}&api_key={}'.format(sample_identifier, api_key)
    request = requests.get(url).json()
    return request

# This function will pull analysis.json data using the sampleID
# This function still needs to be updated to pull the correct data.
def lookup_sampleID(sample_identifier, api_key):
    url = 'https://panacea.threatgrid.com/api/v2/samples/{}/analysis.json?api_key={}'.format(sample_identifier, api_key)
    request = requests.get(url).json()
    return request

# This function will write the returned data to a file
def write_to_file(sample_data, filename):
    out_file = open(filename, 'w')
    out_file.write(json.dumps(sample_data))
    out_file.close()

# This function will pull the sampleID out of the summary report
def get_sample_ID(summary_report):
        return summary_report['data']['items'][0]['item']['sample']


###########################################
# The main calls start here
###########################################
# We will start by echoing the user inputs
talk_to_user(script, sample_identifier, api_key)

# Check if the value given is a SHA256, then pull the summary report
# and write to file
if is_sha256(sample_identifier):
    print(f"The sample identifier is a SHA256: {sample_identifier}")
    summary_report = lookup_sha(sample_identifier, api_key)
    sampleID = get_sample_ID(summary_report)
    print(f"The SampleID is: {sampleID}")
    write_to_file(lookup_sampleID(sampleID, api_key), filename)

# Check if the value given is a SampleID, then pull the report and write to file
elif is_sampleID(sample_identifier):
    print(f"The sample identifier is a SampleID: {sample_identifier}")
    report = lookup_sampleID(sample_identifier, api_key)
    write_to_file(report, filename)

# If the value provided was not a SHA256 or SampleID let the user know
else:
    print("You did not enter a valid SHA26 or SampleID")
