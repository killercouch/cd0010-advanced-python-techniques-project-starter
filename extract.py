"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    NEO_collection = []

    with open(neo_csv_path, 'r') as csv_file:
        csvReader = csv.reader(csv_file)
        next(csvReader)  # scrip the first row (header)
        for line in csvReader:
            NEO_collection.append(NearEarthObject(line[3],
                                                  name=line[4],
                                                  diameter=line[15],
                                                  hazardous=line[7]))
    return NEO_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches_collection = []

    with open(cad_json_path, 'r') as json_file:
        json_data = json.load(json_file)
        for element in json_data['data']:
            approaches_collection.append(CloseApproach(element[0],
                                                       time=element[3],
                                                       distance=element[4],
                                                       velocity=element[7]))
    return approaches_collection
