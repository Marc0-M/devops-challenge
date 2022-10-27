# Lambda integrated with API gateway reading from DynamoDB:

Building Lambda functions that get and post data from and into DynamoDB, and bind these services with API gateway.

------------

### Why use Serverless framework instead of terraform when we need to provision serverless services?
- Less coding efforts with the capability of linking the API gateway with the lambda function.
- No need to use json format when using IAM policies and roles (you can write the permission in raw text and the framework can convert it to json).
- Fewer resources to be written.
- YAML format.

------------
## How to deploy manually:
### Prerequisites:
- AWS cli (Installed & Configured).
- Serverless framework ([how to install](https://www.serverless.com/framework/docs/getting-started/ "how to install"))

### Deployment steps:
- Navigate to folder devops-challenge-main
- Run "serverless deploy"


------------


## Outputs:  
- Services Information.  
- Endpoints:  
		Post link  
		Get link (list all Credentials)  
		Get link (Show all data belong to one of usernames)  
- Lambda functions:  
		Create function  
		List function  
		Get function


------------
## How to use Github actions for CI/CD:
### Prerequisites:
- Have a GitHub account
- Fork and clone this repo (contains code from my previous tutorial)
- Have an AWS account
- Create an AWS IAM user that has the following permissions: IAMFullAccess, AmazonS3FullAccess, CloudWatchFullAccess, AWSCloudFormationFullAccess, AWSLambda_FullAccess and AmazonAPIGatewayInvokeFullAccess.
- Store the AWS user API key and secret key


### Github actions configuration:
- Create a main.yml file to define the workflow configuration under the folder ".github/workflows".
- Add AWS API key and secret key to GitHub secret
	- Go to settings on the forked repo to add your API Key and Secret key. Click on Secrets on the left side nav and click on New repository secret to add your secrets. The API Key and Secret Key gives us programmatic access to your AWS environment.


------------
## How to test the solution:
- From terminal run the following command (also postman could be used):
	- curl --header "Content-Type: application/json" --data '{"username":"xyz","password":"xyz"}' "Post link which has been mentioned in the outputs"
	- You should see (Welcome message, Method, Headers and the body of your request)
- You also can list inserted items using the list link which has been mentioned in the output section.
- If you want to get information about one item, you can use get link followed by the username you want to know about.


------------
## How to clear the solution manually:
- Navigate to folder devops-challenge-main
- Run "serverless remove"
# devops-challenge
