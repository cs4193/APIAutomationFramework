# add your constants here

def base_url():
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


# Update ,PUT , PATCh Delete - Booking ID
def url_patch_put_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)


# same above functions by  using them inside a class as method

class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # Update ,PUT , PATCh Delete - Booking ID
    def url_patch_put_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)


# Making variables and then accessing them
Base_url = "https://restful-booker.herokuapp.com"
