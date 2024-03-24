#! /bin/bash

set -e

if [[ $EUID -ne 0 ]]; then
   echo "Run as root"
   exit 1
fi

DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y postgresql

cp ./configs/pg_ident.conf /etc/postgresql/12/main/pg_ident.conf
cp ./configs/pg_hba.conf /etc/postgresql/12/main/pg_hba.conf
cp ./configs/postgresql.conf /etc/postgresql/12/main/postgresql.conf

sudo systemctl restart postgresql.service
