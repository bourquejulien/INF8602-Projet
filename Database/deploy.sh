#! /bin/bash

set -e

if [[ $EUID -ne 0 ]]; then
   echo "Run as root"
   exit 1
fi

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get upgrade -y && apt-get install -y postgresql

cp ./configs/pg_ident.conf /etc/postgresql/14/main/pg_ident.conf
cp ./configs/pg_hba.conf /etc/postgresql/14/main/pg_hba.conf
cp ./configs/postgress.conf /etc/postgresql/14/main/postgress.conf

sudo systemctl restart postgresql.service
