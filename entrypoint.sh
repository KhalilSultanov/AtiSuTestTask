#!/bin/sh

echo "Start PostgreSQL..."
until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done

echo "Running migrations..."
python manage.py migrate

echo "Running server..."
exec "$@"
