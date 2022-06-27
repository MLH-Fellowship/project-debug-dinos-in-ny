#!/bin/bash

curl --request POST http://127.0.0.1:5000/api/timeline-post/ -d “name=name&email=email&content=content”

curl --request GET http://127.0.0.1:5000/api/timeline-post/
