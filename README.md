
# Investor Bulletin Project

![Welcome](./imgs/hello-welcome.gif)

* Run the Code:
  `docker-compose -f dev_setup/docker-compose.yml up --build`
* Start Celery
  `docker exec -it api-container bash`
  `celery -A worker.app beat --loglevel=info`
  `celery -A worker.app worker --loglevel=info`
* Start subscriber
  `docker exec -it api-container bash`
  `python event_subscriber/main.py`
