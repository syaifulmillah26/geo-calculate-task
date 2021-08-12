from tests.unittest.conf import BaseTestCase


class TestHome(BaseTestCase):
    def setUp(self):
        return super().setUp()

    """ This test is returning value of a distance """

    def test_should_return_float_value(self):
        response = self.client.post(
            '/get-distance',
            data={"destination": "Odintsovo, Russia"}
        )
        result = response.json
        self.assertEqual(type(result.get("distance")), float)

    """
    This test is returning none value as the destination
    is inside the radius of MKAD
    """

    def test_should_return_none(self):
        response = self.client.post(
            '/get-distance',
            data={"destination": "Moscow, Russia"}
        )
        result = response.json
        self.assertEqual(result.get("distance"), None)

    """ This test is validate the empty value of the destination """

    def test_validate_an_empty_value(self):
        response = self.client.post(
            '/get-distance',
            data={"destination": ""}
        )
        result = response.json
        self.assertEqual(result, "Destination could not be empty")

    """ This test is validate the missing coordinates of destination """

    def test_validate_coordinates(self):
        response = self.client.post(
            '/get-distance',
            data={"destination": "Hello! India ( Cafe, Banquet & Halal Meat)"}
        )
        result = response.json
        self.assertEqual(
            result, "Sorry, we could not get the coordinate of this address")
