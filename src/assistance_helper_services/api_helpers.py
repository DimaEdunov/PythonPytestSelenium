import json

import boto3
import requests

from src.parameters.delete_guest_api_parameters import get_cognito_user_pool_id
from src.parameters.guest_parameters import GuestParameters


class ApiHelpers:
    site_code = None
    domain = None

    def __init__(self, application_parameters, key, phone_or_qr, account_type):
        self.domain = application_parameters["domain"]
        self.domain_cart = application_parameters["domain_cart"]
        self.attraction = application_parameters["attraction"]
        self.environment = application_parameters["environment"]
        self.site_code = application_parameters["site_code"]
        self.site_code_cart = application_parameters["site_code_cart"]
        self.country_code = GuestParameters.get_country_code_without_plus_prefix(key)
        self.phone_or_qr = phone_or_qr
        self.account_type = account_type

    def api_get_userid_by_phone_request(self, type):
        if type == "cart_domain":
            ApiHelpers.domain = self.domain_cart
        elif type == "non_cart_domain":
            ApiHelpers.domain = self.domain

        end_point = f'https://api-{self.environment}.pomvom.com/api/v2/users/sign-in/info?phone=%2B{self.country_code}{self.phone_or_qr}&domain={ApiHelpers.domain}'
        print(end_point)

        get_guest_by_phone = requests.get(end_point,
                                          verify=False,
                                          headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                   "x-client-id": "rnd"},
                                          )
        response = json.loads(get_guest_by_phone.content)
        if "'verified': False" in str(response) and self.account_type == "app":
            return None
        else:
            user_id = response['userId']
            return user_id

    def api_get_userid_by_qr_request(self, type):
        if type == "cart_domain":
            ApiHelpers.domain = self.domain_cart
        elif type == "non_cart_domain":
            ApiHelpers.domain = self.domain

        end_point = f'https://api-{self.environment}.pomvom.com/api/v2/users/?qr={self.phone_or_qr}&domain={ApiHelpers.domain}&disableRegex=true'
        print(end_point)

        get_guest_by_phone = requests.get(end_point,
                                          verify=False,
                                          headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                   "x-client-id": "rnd"},
                                          )
        response = json.loads(get_guest_by_phone.content)

        if "Users not found" in str(response):
            return None
        else:
            user_id = response['users'][0]["userId"]
            print("user_id xxx: " + str(user_id))
            return user_id

    def api_create_qr_user_request(self, type):

        if type == "cart_domain":
            ApiHelpers.domain = self.domain_cart
        elif type == "non_cart_domain":
            ApiHelpers.domain = self.domain

        end_point = f'https://api-{self.environment}.pomvom.com/api/v3/accounts'
        print("print end point: " + str(end_point))
        data = {"domain": ApiHelpers.domain,
                "uniqueId": self.phone_or_qr}

        create_qr_user = requests.post(end_point,
                                       headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                "x-client-id": "rnd",
                                                "Content-Type": "application/json"},
                                       data=json.dumps(data),
                                       verify=False)

        response = create_qr_user.status_code
        print(response)

    def api_delete_userid_request(self, user_id_from_get_request, type):
        # If user does not exist, skip the 'DELETE' flow
        if user_id_from_get_request is None:
            pass

        else:
            if type == "cart_domain":
                ApiHelpers.domain = self.domain_cart
            elif type == "non_cart_domain":
                ApiHelpers.domain = self.domain

            end_point = f'https://api-{self.environment}.pomvom.com/api/v3/accounts/{user_id_from_get_request}'
            data = {"domain": ApiHelpers.domain}

            delete_guest = requests.delete(end_point,
                                           headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                    "x-client-id": "rnd",
                                                    "Content-Type": "application/json"},
                                           data=json.dumps(data),
                                           verify=False)

            response = delete_guest.status_code
            print(response)

    def api_get_attraction_name_request(self, type):
        if type == "cart_domain":
            ApiHelpers.site_code = self.site_code_cart
        elif type == "non_cart_domain":
            ApiHelpers.site_code = self.site_code

        end_point = f'https://uk.picasso-api.picsolve.com/config/site/{ApiHelpers.site_code.upper()}?info=AllAttractionInfo'
        print(f'End POINT: {end_point}')

        get_attraction_name_request = requests.get(end_point,
                                                   verify=False,
                                                   headers={"x-api-key": "gxbHGI5F2u6SSd9aoIySuVhWQ142oqF6T1ohdzBb"},
                                                   )
        response = json.loads(get_attraction_name_request.content)
        for dictionary in response:
            for i in dictionary:
                if dictionary[i] == self.attraction.upper():
                    return dictionary['Attraction_Name']

    def api_get_userid_request_opsui(self, type):
        if type == "cart_domain":
            ApiHelpers.domain = self.domain_cart
        elif type == "non_cart_domain":
            ApiHelpers.domain = self.domain

        end_point = f'https://api-{self.environment}.pomvom.com/api/v2/users/?phone=%2B{self.country_code}{self.phone_or_qr}&domain={ApiHelpers.domain}'
        print(end_point)

        get_guest_by_phone = requests.get(end_point,
                                          verify=False,
                                          headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                   "x-client-id": "rnd"},
                                          )
        response = json.loads(get_guest_by_phone.content)
        if "Users not found" in str(response) and self.account_type == "app":
            print("User not found")
            return None
        else:
            users = response['users']
            user_id = users[0]['userId']
            return user_id

    def api_get_another_attraction_name_in_current_park(self):
        end_point = f'https://uk.picasso-api.picsolve-sandbox.com/config/site/{self.site_code.upper()}?info=AllAttractionInfo'

        get_another_attraction_name_request = requests.get(end_point,
                                                           verify=False,
                                                           headers={
                                                               "x-api-key": "gxbHGI5F2u6SSd9aoIySuVhWQ142oqF6T1ohdzBb"},
                                                           )
        response = json.loads(get_another_attraction_name_request.content)
        for dictionary in response:
            print(dictionary)
            if dictionary['Attraction_Code'] != self.attraction.upper() and dictionary['Show_Find_Photo'] == True and \
                    "Video" not in dictionary['Attraction_Name']:
                return dictionary['Attraction_Name'], dictionary['Attraction_Code']

    def api_create_email_user_request(self, email, generated_qr, type):
        end_point = f'https://api-{self.environment}.pomvom.com/api/v3/accounts'
        print("print end point: " + str(end_point))

        if type == "cart_domain":
            ApiHelpers.domain = self.domain_cart
        elif type == "non_cart_domain":
            ApiHelpers.domain = self.domain

        data = {"domain": ApiHelpers.domain,
                "email": email,
                "uniqueId": generated_qr}

        create_email_user = requests.post(end_point,
                                          headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                   "x-client-id": "rnd",
                                                   "Content-Type": "application/json"},
                                          data=json.dumps(data),
                                          verify=False)

        response = json.loads(create_email_user.content)
        print(response)
        if response['accountId']:
            return response['accountId']
        if response['message']:
            assert False

    def api_delete_userid_by_domain(self, user_id, type):
        # If user does not exist, skip the 'DELETE' flow
        if user_id is None:
            print("API Delete - Guest Does not exist, Delete was not submitted")
            pass

        else:
            if type == "cart_domain":
                ApiHelpers.domain = self.domain_cart
            elif type == "non_cart_domain":
                ApiHelpers.domain = self.domain

            end_point = f'https://api-{self.environment}.pomvom.com/api/v2/users/{user_id}?deleteMediaAssociations=true&domain={ApiHelpers.domain}'
            print("print end point: " + str(end_point))
            data = {"domain": self.domain}

            delete_guest = requests.delete(end_point,
                                           headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                    "x-client-id": "rnd",
                                                    "Content-Type": "application/json"},
                                           data=json.dumps(data),
                                           verify=False)

            response = delete_guest.status_code
            print(response)

    def api_get_userid_by_email_request(self, email, type):
        if type == "cart_domain":
            ApiHelpers.domain = self.domain_cart
        elif type == "non_cart_domain":
            ApiHelpers.domain = self.domain

        end_point = f'https://api-{self.environment}.pomvom.com/api/v2/users/?email={email}&domain={ApiHelpers.domain}'
        get_guest_by_email = requests.get(end_point,
                                          verify=False,
                                          headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                   "x-client-id": "rnd"},
                                          )

        response = json.loads(get_guest_by_email.content)
        user_id = response['users'][0]['userId']
        print("user_id in email get: " + str(user_id))
        return user_id

    def api_get_media_id_by_date(self, attraction_code, epoch_from_time, epoch_to_time,
                                 list_of_media_ids, type):
        # GET media : api/v5/media, filtered by 'from' and 'to' time, based on file CreateTime - TimeStamp
        end_point = f'https://api-{self.environment}.pomvom.com/api/v5/media?domain={ApiHelpers.domain}&attractionCode={attraction_code.upper()}&fromTime={epoch_from_time * 1000}&toTime={epoch_to_time * 1000} '
        print("Send GET to : " + str(end_point))

        get_media_id = requests.get(end_point,
                                    verify=False,
                                    headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa", "x-client-id": "rnd"},
                                    )

        response = json.loads(get_media_id.content)
        print("GET Response : " + str(response) + "\n")

        # Parsing response, extracting mediaIds', adding them into a list

        # media_id_counter

        cell_end_index = len(list_of_media_ids)

        media_id_counter = 0
        cell_start_index = cell_end_index
        try:
            for index in range(len(response["media"])):
                print("media id found '%s', createTime: %s - #%s" % (
                    response["media"][index]["mediaId"], response["media"][index]["createTime"], index + 1))
                list_of_media_ids.append(response["media"][index]["mediaId"])

                media_id_counter += 1
                cell_end_index += 1

            print("\n")

            # data
            print("media_id counter - total : " + (str(len(list_of_media_ids))))
            print("media_id counter - this bulk : " + (str(media_id_counter)))
            print("Cell start index - " + str(cell_start_index))
            print("Cell end index - " + str(cell_end_index))

            media_id_counter = 0

            return {"start_index": cell_start_index,
                    "end_index": cell_end_index,
                    "media_ids_this_bulk": media_id_counter,
                    "total amount of media_ids": len(list_of_media_ids)}

        except KeyError:
            print("No photos found in this cycle", "No photos found in this cycle")

    def api_post_associate_media_to_user_id(self, user_id, media_ids, type):
        if type == "cart_domain":
            ApiHelpers.domain = self.domain_cart
        elif type == "non_cart_domain":
            ApiHelpers.domain = self.domain

        end_point = f'https://api-{self.environment}.pomvom.com/api/v5/media/accounts/{user_id}'

        data = {"domain": ApiHelpers.domain,
                "mediaIds": media_ids}

        associate_media_to_guest = requests.post(end_point,
                                                 headers={"x-api-key": "e4311492-4fcd-4aa1-93b8-df26a33f23fa",
                                                          "x-client-id": "rnd",
                                                          "Content-Type": "application/json"},
                                                 data=json.dumps(data),
                                                 verify=False)

        print(associate_media_to_guest.status_code)
        response = json.loads(associate_media_to_guest.content)

        print(response)

        print(f"Association to user: {user_id} to media ID: {media_ids}")
