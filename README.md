# Slack Bot Template

More of a plan than anything.

A bot template that aims to help speed up the bot creation process.

## Setup

### Slack

To create a bot with slack you need to log in.
https://api.slack.com

### Environment Variables

 - SLACK_OAUTH
 - DEPLOYMENT
 - CI_CD
 

## CI/CD

### Travis
Travis will be used for all these steps to make things easier.


## Hosting

### Deploying to IBM Cloud Cloudfoundary

To get a basic bot running as an IBM Cloudfoundary app you just need to update .travis.yml
Below is a sample with options. 
If you are a **federated user** ( e.g. IBMers ) you will need to generate an IAM Key and provide that as your password.
You can generate a key [here](https://console.bluemix.net/docs/iam/userid_keys.html#userapikey?cm_sp=dw-bluemix-_-recipes-_-devcenter)

    deploy:
      edge: true
      provider: bluemixcloudfoundry
      username: [my_user_name | apikey]
      password: [ my_password | IAM-API-KEY ]
      organization: my_org_name
      space: my_space
      manifest: manifest.yml     # (optional)  Defaults to manifest.yml.
      app_name: Ask-River        # (optional)
      region: [ng | eu-gb | au-syd]                       # (optional)  [ng, eu-gb , au-syd] Defaults to US South region (ng).
      api: https://api.ng.bluemix.net

Environemnt variables required to start app.
 
 - One of the following
    - bluemix_username & bluemix_username ( non-federated standard users)
    - bluemix_iam_apikey   ( federated/SSO users )
 - bluemix_organization
 - bluemix_space
 - bluemix_region
 - application_name
 
 
 The files of interest for deploying to IBM Cloud Foundary are:
 
  - **Procfile** Instructs CF how to start the application
  - **runtime.txt** Informs CF which [supported Python version](https://github.com/cloudfoundry/python-buildpack/releases) to use
  - **manifest.yml** Contains application metrics like allocated size, ram, name etc.

### Deploying to AWS

Assuming you're [familiar with the process](https://medium.com/@itsdavidthai/comprehensive-aws-ec2-deployment-with-travisci-guide-7cafa9c754fc),
we can easiliy make some quick changes and deploy out bot to EC2 rather quickly.

### Deploying to Azure
Test

### Deploying to Heroku

