# sqsp-lambda
Stores a webhook listener Lambda Function intended to process orders from Squarespace's Commerce Webhook API.

## Project Overview

Squarespace's Commerce feature offers a Webhook service in which they will execute a `POST` request upon `Order create` and `Order update` actions. This project leverages that feature to set up an AWS API Gateway -> Lambda Webhook listener that will eventually process the inbound requests and do other things.

Currently, though, this function only saves the totality of the body (in `json` format) to a pre-defined S3 bucket.

> **REF:** <https://developers.squarespace.com/webhooks/overview>