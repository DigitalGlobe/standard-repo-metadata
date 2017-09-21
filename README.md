# Example of metadata files required of all repos

## Service information file.
Name: ```<service-name>.info.yml``` <br>
Required: ```true```<br>
Contents:  Contains metadata about the service or component including points of contact, URLs, documentation, etc.<br>

## Service API Specification
Name: ```<service-name>.swagger.yml``` <br>
Required: ```required for RESTful services```<br>
Contents:  A Swagger 2.0 API specification for the service<br>

## CI/CD Deployment information
Name: ```<service-name>.deployment-variables.yml```<br>
Required: ```required for items deployed via the common pipeline.```<br>
Contents: This will contain processing instructions for the CI/CD pipeline. <br> 
Items such as the following will be specificed in this file
* OAuth2 Scopes required by the service at runtime
* Should the service be deployed to prod (we have some test-helpers and such that dont get deployed to prod.)
* Database requirements
* S3 requirements
* Export & installation restrictions


## Multiple services in a single repo
Repeat all required files for the second service, just use the second services name in place of ```<service-name>```

