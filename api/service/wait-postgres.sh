#!/bin/sh

URL="postgresql://$POSTGRES_USER:$POSTGRES_DB@$DB_HOST:5432"
echo $URL

status=1
while [ $status -gt 0 ]
do
  psql "$URL" -c "\q" > /dev/null 2>&1
  status=$?
  sleep 1
  echo "Postgres is unavailable - sleeping, and retrying"
done
echo "Postgres is up - executing command"
