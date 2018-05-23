"""
A module to get information about the next departure from a stop.
This code is released under the terms of the MIT license. See the LICENSE
file for more details.
"""
import requests

class Ruter:
    """This class is used to get departure information from Ruter."""
    BASE_URL = 'http://reisapi.ruter.no/StopVisit/GetDepartures/'

    def __init__(self):
        """Initialize"""
        self.stopInfo = False
    def getDepartureInfo(self, stopid):
        """Get departure info from stopid."""
        fetchurl = self.BASE_URL + str(stopid)
        try:
            departureRequest = requests.get(fetchurl, timeout=2).json()[0]
        except:
            stopInfo = False
        else:
            departureResponse = departureRequest['MonitoredVehicleJourney']
            line = departureResponse['LineRef']
            destination = departureResponse['DestinationName']
            time = departureResponse['MonitoredCall']['ExpectedDepartureTime']
            stopInfo = [time, line, destination]
        return stopInfo