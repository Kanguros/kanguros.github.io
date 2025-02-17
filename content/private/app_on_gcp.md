Title: AppWeb on GCP
Date: 2024-10-05
Status: draft
Category: Private
Summary: Web application developed in Flask deployed on Google Cloud Platform.

To modify values from the web, there has to be somekind of database.
Code will have to be modified in order to handle it. It shouldn't be difficult.

## How to in Python

```python
# Imports the Google Cloud client library
from google.cloud import datastore

# Instantiates a client
datastore_client = datastore.Client()

# The kind for the new entity
kind = "Task"
# The name/ID for the new entity
name = "sampletask1"
# The Cloud Datastore key for the new entity
task_key = datastore_client.key(kind, name)

# Prepares the new entity
task = datastore.Entity(key=task_key)
task["description"] = "Buy milk"

# Saves the entity
datastore_client.put(task)

print(f"Saved {task.key.name}: {task['description']}")
```

## Is there a human friendly GUI for datastore?

There is.

https://cloud.google.com/datastore/docs/console/managing-datastore

![[Pasted image 20241004172631.png]]

## How much does it cost?

Nothing? Looks like it

https://cloud.google.com/appengine/docs/legacy/standard/python/quotas#Datastore

## Pipeline for deployment

As we store code on GitHub, we can use GitHub Actions. Quick Google gave me that: https://medium.com/geekculture/deploy-to-google-app-engine-using-github-actions-ci-cd-f25d4c965fbc

```yaml
# This is a basic workflow to help you get started with Actions

name: Deploy to GAE

# Controls when the workflow will run
on:
    # Triggers the workflow on push or pull request events but only for the main branch
    push:
        branches: [main]
    pull_request:
        branches: [main]

    # Allows you to run this workflow manually from the Actions tab
    workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
    deploy:
        name: Deploying to Google Cloud
        runs-on: ubuntu-latest

        steps:
            - name: Checkout
              uses: actions/checkout@v2

            - name: Deploy to App Engine
              id: deploy
              uses: google-github-actions/deploy-appengine@v0.2.0
              with:
                  deliverables: app.yaml cron.yaml
                  version: v1
                  project_id: ${{ secrets.GCP_PROJECT }}
                  credentials: ${{ secrets.GCP_CREDENTIALS }}

            - name: Test
              run: curl "${{ steps.deploy.outputs.url }}"
```
