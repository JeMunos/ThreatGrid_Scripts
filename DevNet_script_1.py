# ThreatGrid DevNet Learning Lab Lesson 3 Part 1
# This script will take a SHA256 and obtain the
# ThreatGrid sampleID
import requests

sha256 = '<sha256>'
tg_api_key = '<api_key>'

# This function will get the summary report for a SHA256
def lookup_sha(sha256, api_key):
    url = 'https://panacea.threatgrid.com/api/v2/search/submissions?q={}&api_key={}'.format(sha256, tg_api_key)
    request = requests.get(url).json()
    return request

# This function will pull the sampleID out of the summary report
def get_sample_ID(summary_report):
        return summary_report['data']['items'][0]['item']['sample']

########################
# Main calls start here
########################

# Lets get the summary report from ThreatGrid
summary_report = lookup_sha(sha256, tg_api_key)
print(f"This is what the summary report looks like: {summary_report}")

# Now lets extract the sample ID from the summary report
sampleID = get_sample_ID(summary_report)
print(f"This is the SampleID: {sampleID}")
