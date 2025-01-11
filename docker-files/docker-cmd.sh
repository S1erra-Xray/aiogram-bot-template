#!/usr/bin/env bash

redis-server --daemonize yes

function exec_pg_user() {
	su postgres -c "$1"
}

function pg_init_and_start() {
	exec_pg_user "initdb && pg_ctl start && createdb $POSTGRES_DB"
}

if [[ $TYPE == "debug" ]]; then
	pg_init_and_start
elif [[ $TYPE == "release" ]]; then
	pg_init_and_start
#	exec_pg_user "psql -U postgres -W"
fi

poetry run python /home/bot/bot.py
sleep 100000
