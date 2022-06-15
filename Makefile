.PHONY: clean build-docker-local build-docker-dev run-docker-local kill-ports stop-chatbot-docker

clean:
		find . -name '*.pyc' -exec rm -rf {} +
		find . -name '*.pyo' -exec rm -rf {} +
		find . -name '*~' -exec rm -rf  {} +
		find . -name '*.mypy' -exec rm -rf  {} +
		find . -name '*__pycache__' -exec rm -rf  {} +
		rm -rf build/
		rm -rf .mypy_cache/
		rm -rf dist/
		rm -rf docs/build
		rm -rf docs/.docusaurus

build-docker-local:
		@echo "Building docker image local"
		cd chatbot && docker build -t chatbot:latest .

build-docker-dev:
		@echo "Building docker image dev"
		cd chatbot && docker build -t registry-intl.ap-southeast-5.aliyuncs.com/mti-portal-dev/chat-bot:test .
		@echo "Login to docker registry"
		cat chatbot/scripts/ali_pass.txt | docker login --username=devdashboard@5550576154359067 registry-intl.ap-southeast-5.aliyuncs.com --password-stdin
		@echo "Pushing docker image to registry"
		docker push registry-intl.ap-southeast-5.aliyuncs.com/mti-portal-dev/chat-bot:test

run-docker-local:
		@echo "Running docker image local"
		docker run -p 5000:5000 -t chatbot:latest

kill-ports:
		kill -9 `sudo lsof -t -i:5005` \
		&& \
		kill -9 `sudo lsof -t -i:5055` \
		&& \
		sudo kill -9 `sudo lsof -t -i:8888` \

stop-chatbot-docker:
		@echo "Stopping docker image local"
		# docker stop $(docker ps -q --filter ancestor=chatbot:latest )
		docker ps --filter name=chatbot --filter status=running -aq | xargs docker stop

format-chatbot:
		cd chatbot && black  . && isort .

run-chatbot:
		@echo "Running chatbot"
		cd chatbot && poetry run chatbot_mti run -m models/ \
		--endpoints conf/endpoints.yml \
		--port 5005 \
		--cors '*' \
		--enable-api \
		--debug \
		--credentials conf/credentials.yml

run-actions:
		@echo "Running actions"
		cd chatbot && poetry run python3 -m rasa_sdk --actions actions
