#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

import json
import requests

DOCKER_REGISTRY = os.environ.get('DOCKER_REGISTRY', 'hub.docker.com')
DOCKER_NAMESPACE = os.environ.get('DOCKER_NAMESPACE', 'betacloud')
DOCKER_IMAGE = os.environ.get('DOCKER_IMAGE', None)

def get_tags_from_all_images():
    response = requests.get("https://%s/v2/repositories/%s?page_size=200" %(DOCKER_REGISTRY, DOCKER_NAMESPACE))

    images = response.json()['results']
    for image in images:
        get_tags_from_image(image)


def get_tags_from_image(image):
    response = requests.get("https://%s/v2/repositories/%s/%s/tags/" % (DOCKER_REGISTRY, DOCKER_NAMESPACE, image['name']))
    for tag in response.json()['results']:
        print "%s/%s:%s" % (image['namespace'], image['name'], tag['name'])


def get_tags_of_image(image):
    response = request("GET", "%s/%s/tags/list" % (DOCKER_NAMESPACE, image))
    return response.json()['tags']


if __name__ == "__main__":
    if DOCKER_IMAGE:
        get_tags_from_image(DOCKER_IMAGE)
    else:
        get_tags_from_all_images()
