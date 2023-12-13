# #!/bin/bash
# set -e

if [ -z "$1" ]; then
  echo "Required generator file is missing."
  exit 1
fi

file="$1"

npm install @openapitools/openapi-generator-cli -g

mkdir temp
rm -rf ./generated
rm -rf ./docs/generated

openapi-generator-cli generate \
  -i "$file" \
  -g python \
  -o ./temp \
  --additional-properties=modelPropertyNaming=original

mv ./temp/docs ./docs/generated
mv ./temp/README.md ./docs/generated

mv ./temp/openapi_client ./generated

rm -rf ./temp

