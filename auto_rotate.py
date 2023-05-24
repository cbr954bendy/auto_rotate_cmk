import boto3 

def lambda_handler(event, context):
    client = boto3.client('kms')
    # get a list of all kms keys
    response = client.list_keys()
    cmk_list = response['Keys']

    # iterate over the key list to get the Key Ids
    for cmk in cmk_list:
        key_id = cmk['KeyId']

        # finally enable the rotation
        try: 
            client.enable_key_rotation(KeyId=key_id)
            print(f"Automatic rotation enabled for Key: {key_id}.")
        except Exception as e:
            print(f"Error enabling key rotation for CMK: {key_id}. Error: {str(e)}")





