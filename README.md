# auto_rotate_cmk
Checks CMK's and enables auto rotation

This will consist of a CloudFormation template that can be deployed to any account and region. There will be a Lambda function that iterates through a list of AWS KMS Customer Master Key's and if they are not set to auto rotate, it will be enabled by the function. 

Enabling auto-rotation does not impact existing encyrpted objects even after key rotation as the Key ID does not change, only the underlying key material, while the old key material is retained.

This in it's current configuration will be invoked by a periodic Event Bridge Rule. 
