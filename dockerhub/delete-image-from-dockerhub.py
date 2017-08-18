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

import requests


try:
    DOCKER_REGISTRY = os.environ.get('DOCKER_REGISTRY', 'hub.docker.com')

    DOCKER_REGISTRY_USERNAME = os.environ['DOCKER_REGISTRY_USERNAME']
    DOCKER_REGISTRY_PASSWORD = os.environ['DOCKER_REGISTRY_PASSWORD']
    DOCKER_IMAGE = os.environ['DOCKER_IMAGE']
except KeyError:
    sys.exit(1)


if __name__ == "__main__":
    response = requests.post("https://%s/v2/users/login" % DOCKER_REGISTRY, json={"username": DOCKER_REGISTRY_USERNAME, "password": DOCKER_REGISTRY_PASSWORD})
    token = response.json()['token']
    response = requests.delete(
        "https://%s/v2/repositories/%s" % (DOCKER_REGISTRY, DOCKER_IMAGE),
        headers={"Authorization": "JWT %s" % token}
    )
    print response
