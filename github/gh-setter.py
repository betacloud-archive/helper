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

from github import Github
import yaml

try:
    GH_USERNAME = os.environ['GH_USERNAME']
    GH_PASSWORD = os.environ['GH_PASSWORD']
except KeyError:
    sys.exit(1)

with open('gh-setter.yml') as fp:
    CONFIG = yaml.load(fp)

gh = Github(GH_USERNAME, GH_PASSWORD)

for organization in CONFIG:
    data = CONFIG[organization]
    for repository in gh.get_organization(organization).get_repos():
        print repository.name
        repository.edit(
            has_downloads=data['has_downloads'],
            has_wiki=data['has_wiki'],
            homepage=data['homepage']
        )
