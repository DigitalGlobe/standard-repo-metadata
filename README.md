# standard-repo-metadata
Example of metadata files required of all DG repos (under construction)


```.digitalglobe.yml``` - required.  Contains metadata about the service or component including points of contact, URLs, documentation, etc.

```.service2.yml``` - optional - another service that lives in this repo
# MWATERS EDITIORIAL - This (service2) is a violation of good coding practices.  1 repo=1 service.  Combining them is problematic.  E.g. do a change to service2, and service 1 will get re-deployed (which is not needed).  I advocate that this be removed.  Note that of the 12-factors, this is #1.

```.api-spec.yml``` - optional - swagger api spec
# MWATERS EDITORIAL - I think this should be swagger.yml - that is the industry standard for this filename
