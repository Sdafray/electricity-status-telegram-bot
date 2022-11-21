ENV_FILE='.env'

if [ ! -f "$ENV_FILE" ]; then
  echo "You must create file '$ENV_FILE'"
  return
fi

poetry export -o requirements.txt --without-hashes
docker compose up --build -d