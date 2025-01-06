# #!/bin/bash
# set -e

if [ -z "$1" ]; then
  echo "Required generator file is missing."
  exit 1
fi

rm -rf ./passageidentity/openapi_client

file="$1"

docker run --rm -v "${PWD}:/local" -u $(id -u) openapitools/openapi-generator-cli:latest generate \
  -i "/local/$file" \
  -g python \
  -o /local/temp \
  --additional-properties=modelPropertyNaming=original,packageName=passageidentity.openapi_client \
  --global-property apiTests=false,modelTests=false,apiDocs=false,modelDocs=false \
  --model-name-mappings CreateUserRequest=CreateUserArgs,UpdateUserRequest=UpdateUserArgs,UserInfo=PassageUser

mv ./temp/passageidentity/openapi_client ./passageidentity/openapi_client
rm -rf ./temp
