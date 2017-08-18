#!/usr/bin/env bash
set -x

# Available environment variables
#
# DOCKER_IMAGE_TAG
# DOCKER_NAMESPACE

python dockerhub/list-all-image-tags-from-dockerhub.py | grep $DOCKER_IMAGE_TAG > $DOCKER_IMAGE_TAG.lst

while read image; do
    image_name=$(echo $image | awk -F: '{ print $1 }' | awk -F/ '{ print $NF }')
    docker run --rm -t $image dpkg-query -f '${binary:Package}\n' -W > $image_name.packages
    docker rmi -f $image
done < $DOCKER_IMAGE_TAG.lst

sort *.packages | uniq >> $DOCKER_IMAGE_TAG.packages
