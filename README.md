# Legacy geows.ds.iris.edu (discontinued)

This repository contains web content previously found at geows.iris.washington.edu.

The content here is no longer maintained.

## Markdown Rendering of Main Web Page 
#### (source: index.html - links have changed)


### GeoWS Project

#### GeoWS Overview

The GeoWS approach is to enable search, discovery, and data access across widely varying
data provider content by using a consistent pattern for constructing query URLs.

Funded project partners include: Caltech, Columbia, IRIS, UCSD/SDSC, Unidata

More information: GeoWS earthcube.org project page [http://earthcube.org/group/geows-geoscience-web-services]

#### Technical Information and Downloads

* GeoWS Service Template and GeoCSV documents. [`/documents`]
* Create GeoWS services with Web Service Shell [https://github.com/iris-edu/webserviceshell]
    * Rapidly implement using Tomcat, configuration files and existing data retrieval programs
    * Can be extended with custom Java code

Web Service Shell Documentation explains concepts of operation, provides preliminary
configration files and an example implementation. The example implementation includes
a python “handler” illustrating a data retreival program. [`/WSS2-Seiscode/wss2_example.html`]

#### GeoWS-Style Services

Multiple services were developed to illustrate and test the concepts of GeoWS query
patterns and to use GeoCSV output for the highest value information.

##### Funded Partner Developed GeoWS Services
[`/endpoints`]

##### Unfunded Collaborator Services

The approach taken to illustrate interoperating services is for IRIS DMC to build prototype
services on behalf of each unfunded collaborator respectively. Selected data is accessed
in its native form and query patterns, then reformated and returned to the requesting client.
The general process is:

* Web Service Shell is used to build the core services (Samples of Unfunded Services)[`/quick_links`]

* A Swagger framework (GeoWS Swagger Services)[`/geows-uf`] is layered on top of the respective web services to:
    * evaluate standardized API documentation using Swagger Specification
    * and evaluate URL building and data retrieval using swagger-ui

##### To Build an Unfunded GeoWS URL:

* Use the GeoWS Swagger Services page to start [`/geows-uf`]
    
* Select one of the services by name and select the “HEAD” operation
    
* select the “Try it out” button near the bottom of page
    
* _Alternatively_ – use “GET” to return data and build the respective URL


