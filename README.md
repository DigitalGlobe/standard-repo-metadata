# Example of metadata files required of all repos

## Service information file.
Name: ```<service-name>.info.yml``` 
Required: ```true```
Contents:  Contains metadata about the service or component including points of contact, URLs, documentation, etc.

## Service API Specification
Name: ```<service-name>.swagger.yml``` 
Required: ```required for RESTful services```
Contents:  A Swagger 2.0 API specification for the service

## CI/CD Deployment information
Name: ```<service-name>.deployment-variables.yml```
Required: ```required for items deployed via the common pipeline.```
Contents: This will contain processing instructions for the CI/CD pipeline.  Items such as the following will be specificed in this file
* For example we create a new user from scratch every time with only the scopes listed here.  
* Should the service be deployed to prod (we have some test-helpers and such that dont get deployed to prod. 
* Does the service require a database?
* Does the service require S3 credentials?
* Does the service require ITAR access? (If it isnt in the ITAR org, this is an ERROR)


## Multiple services in a single repo
Repeat all required files for the second service, just use the second services name in place of ```<service-name>```

