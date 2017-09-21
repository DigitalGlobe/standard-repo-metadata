# standard-repo-metadata
Example of metadata files required of all DG repos (under construction)


```servicename.info.yml``` - required.  Contains metadata about the service or component including points of contact, URLs, documentation, etc.

```servicename2.info.yml``` - optional - another service that lives in this repo

```servicenamne.swagger.yml``` - optional - swagger api spec

```servicename.deployment-variables.yml``` - required for things deployed via the common pipeline.  
This will contain processing instructions for the CI/CD pipeline.  Things like
* For example we create a new user from scratch every time with only the scopes listed here.  
* Should the service be deployed to prod (we have some test-helpers and such that dont get deployed to prod. 
* Does the service require a database?
* Does the service require S3 credentials?
* Does the service require ITAR access? (If it isnt in the ITAR org, this is an ERROR)

