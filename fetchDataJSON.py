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
ENDPOINT = 'https://adamdill.com/users'
HEADERS = {
    'client_id':'1234',
    'client_secret':'1234',
    'x-coorelation-id':f"{uuid.uuid4()}",
}


def main(argv):
    # default output file name
    outputfile = 'output.csv'
    response = requests.get(ENDPOINT, headers=HEADERS).json()
    users = response['users']
    
    try:
        opts, args = getopt.getopt(argv,"ho:",["ofile="])
    except getopt.GetoptError:
        print("fetchDataJSON.py -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("fetchDataJSON.py -o <outputfile>")
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    writeFile(outputfile, users)


def writeFile(out, users):
    data_file = open(out, 'w')
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    
    for user in users:
        if count == 0:
            # Writing headers of CSV file
            header = user.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(user.values())


if __name__ == "__main__":
   main(sys.argv[1:])