from geopy.geocoders import Nominatim
from geopy import distance
from app.tools.logger import log_info


class HomeHelpers:
    def __init__(self, destination=None):
        self.destination = destination

    def check_distance(self):
        try:
            """
                checking the destination value whether empty or not
                if empty then it return false otherwise it will pass
            """
            if not self.destination:
                return False, "Destination could not be empty"

            """
                set default latitude and longitute of Moscow Ring Road and Central Moscow
                source https://www.google.com/maps
                return latitude and longitute as tuple data type

                count the radius from central moscow to MKAD
                from more information about getting the radius please visit:
                https://www.calcmaps.com/map-radius/
            """
            origin = (55.691070550537766, 37.41304316517711)
            moscow = (55.77229792971136, 37.6276093224397)
            radius = 15.71  # km,

            """
                use geocoder library to get the latitude and longitude of destination
            """
            geocoder = Nominatim(user_agent="Geo Calculate")
            coordinates = geocoder.geocode(self.destination)

            """ ensure coordinates is not empty """
            if not coordinates:
                return False, "Sorry, we could not get the coordinate of this address"

            """
                get latitude and longitude of destination and
                return it as tuple data type
            """
            destination = (coordinates.latitude, coordinates.longitude)

            """
                checking the distance between moscow and destination find the radius
            """
            r_destination = format(distance.distance(
                moscow, destination).km, ".2f")

            """
                get the distance between origin and destination
                use distance from geopy to check the distance between:
                origin and destination
            """
            result = format(distance.distance(origin, destination).km, ".2f")

            """
                returning data with if and else statement
                if the radius from central moscow to destination is greater than
                radius from central moscow to MKAD then it returning the distance,
                otherwise it return an empty distance
            """
            data = dict()
            data["message"] = "Ok"
            data["distance"] = float(result) if float(
                r_destination) > radius else None

            """ save log results """
            log_info(float(result), "logs/results.log")

            return True, data

        except Exception as e:
            raise Exception(e)
