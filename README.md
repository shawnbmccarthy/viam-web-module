# Viam Code Deploy Demo

simple web module to show how we can deploy a flask object

## Overview

Viam has a module registry, the question is can we deploy a simple web-app to
my robot which hosts a very simple page right now using the module registry.

The core requirements: 
1. the web-app must not live in the same github repository as the module
2. the web-app must provide an install script called install.sh
2. this web module must not have any hard-coded artifacts about the repo
3. this web module should have a basic sensor which can validate the web-app is up

## github action
The github action will drive the release of the code

## TODO
1. documentation
2. validate generalization of code
3. testing

## Reference
1. [viam-web-demo](https://github.com/shawnbmccarthy/viam-web-demo/)

# Support

Contributions are welcome in the form of issues and pull request, any support needs
please email me at:
[shawn@viam.com](mailto:shawn@viam.com)