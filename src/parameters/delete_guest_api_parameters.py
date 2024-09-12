import os

import boto3


def get_cognito_user_creds():

    creds = {'access_key' : 'AKIAZDMJ5MLUOO6Y6CJP' , 'secret_access_key' : os.environ.get('cognito_secret_access_key')}
    return creds


def get_cognito_user_pool_id(key):
    user_pool_id = {'test' : os.environ.get('user_id_pool_test'), 'se1' : os.environ.get('user_id_pool_se1')}


    return user_pool_id[key]


def cognito_delete_guest(cognito_credentials, user_id, region):
    print(user_id)
    region_name = "eu-west-2"

    client = boto3.client('cognito-idp',
                          aws_access_key_id=cognito_credentials['access_key'],
                          aws_secret_access_key=cognito_credentials['secret_access_key'],
                          region_name=region_name
                          )

    response = client.admin_delete_user(
        UserPoolId=get_cognito_user_pool_id(region),
        Username=user_id)
    print("Cognito debug C")
    print(response)
