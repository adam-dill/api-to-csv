#
#   Calls an api and converts the reponse to CSV.
#   For simple JSON data consisting of key and 
#   value pairs, keys will be headers for the CSV 
#   file and values the descriptive data.
#
#   args: 
#   [OPTIONAL] -o <outputfile>
#
import sys, getopt
import requests
import csv
import uuid

# Define the api and headers
ENDPOINT = 'https://adamdill.com/users/csv'
HEADERS = {
    'client_id':'1234',
    'client_secret':'1234',
    'x-coorilation-id':f"{uuid.uuid4()}",
}


def main(argv):
    # default output file name
    outputfile = 'output.csv'
    response = requests.get(ENDPOINT, headers=HEADERS)
    
    try:
        opts, args = getopt.getopt(argv,"ho:",["ofile="])
    except getopt.GetoptError:
        print("fetchDataCSV.py -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("fetchDataCSV.py -o <outputfile>")
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    writeFile(outputfile, response)


def writeFile(out, response):
    with open(out, 'w') as f:
        writer = csv.writer(f)
        for line in response.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))


if __name__ == "__main__":
   main(sys.argv[1:])