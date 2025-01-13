docker run --rm \
  -v ${PWD}:/local \
  openapitools/openapi-generator-cli generate \
  -i https://ticktick.com/openapi.yaml \
  -g python-pydantic-v1 \
  -o /local/ \
  -c /local/config.json
