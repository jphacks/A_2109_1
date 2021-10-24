until mysqladmin ping -h db --silent; do
  echo 'waiting for mysqld to be connectable...'
    sleep 2
    done

    echo " DB is started!"
    python3 run.py
