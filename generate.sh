# #!/bin/bash
# set -e

if [ -z "$1" ]; then
  echo "Required generator file is missing."
  exit 1
fi

file="$1"

npm install @openapitools/openapi-generator-cli -g

mkdir temp
rm -rf ./passageidentity/openapi_client
rm -rf ./docs/generated

openapi-generator-cli generate \
  -i $file \
  -g python \
  -o ./temp \
  --additional-properties=modelPropertyNaming=original,packageName=passageidentity.openapi_client

mv ./temp/docs ./docs/generated
mv ./temp/README.md ./docs/generated

mv ./temp/passageidentity/openapi_client ./passageidentity/openapi_client

rm -rf ./temp

