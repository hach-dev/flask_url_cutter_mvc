#!/bin/sh

set -o errexit
set -o nounset

postgres_ready() {
  python <<END
import sys
import psycopg2

try:
    psycopg2.connect("${DATABASE_URL}")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  echo >&2 'Waiting for PostgreSQL to become available...'
  sleep 1
done
echo >&2 'PostgreSQL is available'


exec "$@"
