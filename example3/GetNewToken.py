import boto3
import getpass

# Datos del pool existente
pool_id = input("Enter Pool ID (ej: us-east-1_EgofrrpPW): ")
client_id = input("Enter Client ID (ej: 1e7747c4uqci0gts6b0j5fc4aa): ")
username = input("Enter Username: ")
password = getpass.getpass("Enter Password (will be hidden): ")

region = 'us-east-1'

cognito = boto3.client('cognito-idp', region_name=region)

print("Authenticating...")
try:
    auth_response = cognito.initiate_auth(
        ClientId=client_id,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )

    access_token = auth_response['AuthenticationResult']['AccessToken']
    id_token = auth_response['AuthenticationResult']['IdToken']
    refresh_token = auth_response['AuthenticationResult']['RefreshToken']
    expires_in = auth_response['AuthenticationResult']['ExpiresIn']

    print("\n✅ Authentication successful!")
    print(f"Token expires in: {expires_in} seconds ({expires_in // 60} minutes)")
    print(f"\nAccess Token (Bearer Token):\n{access_token}")
    print(f"\nID Token:\n{id_token}")

except cognito.exceptions.NotAuthorizedException as e:
    print(f"❌ Authentication failed: Invalid username or password")
except Exception as e:
    print(f"❌ Error: {e}")
