# #!/bin/bash
# set -e

if [ -z "$1" ]; then
  echo "Required generator file is missing."
  exit 1
fi

rm -rf ./passageidentity/openapi_client
rm -rf ./docs

file="$1"

docker run --rm -v "${PWD}:/local" -u $(id -u) openapitools/openapi-generator-cli:latest generate \
  -i "/local/$file" \
  -g python \
  -o /local/temp \
  --additional-properties=modelPropertyNaming=original,packageName=passageidentity.openapi_client \
  --model-name-mappings CreateUserRequest=CreateUserArgs,UpdateUserRequest=UpdateUserArgs,UserInfo=PassageUser

mv ./temp/docs ./docs
mv ./temp/README.md ./docs

mv ./temp/passageidentity/openapi_client ./passageidentity/openapi_client

rm -rf ./temp
