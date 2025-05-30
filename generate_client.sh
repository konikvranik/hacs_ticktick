docker run --rm \
  -v ${PWD}:/local \
  --user $(id -u):$(id -g) \
  openapitools/openapi-generator-cli generate \
  -i https://ticktick.com/openapi.yaml \
  -g python-pydantic-v1 \
  -o /local/ \
  -c /local/client_config.json \
  --log-to-stderr \
  --global-property debugOperations