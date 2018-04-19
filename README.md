# Docker
- Windows
1. Install Docker Toolbox for Windows
2. Run Docker QuickStart

- Linux
1. Install Supported storage drivers
`sudo apt-get update`
`sudo apt-get install \
    linux-image-extra-$(uname -r) \
    linux-image-extra-virtual`
2. Set uo the repository
`sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common`
3. Install Docker
`sudo apt install docker.io`

- Docker machine
1. Install docker machine
* Linux
`base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/tmp/docker-machine &&
  sudo install /tmp/docker-machine /usr/local/bin/docker-machine`
* Windows using GitBash
`base=https://github.com/docker/machine/releases/download/v0.14.0 &&
  mkdir -p "$HOME/bin" &&
  curl -L $base/docker-machine-Windows-x86_64.exe > "$HOME/bin/docker-machine.exe" &&
  chmod +x "$HOME/bin/docker-machine.exe"`
# Add token to Git
2. Create docker-machine: `docker-machine --github-api-token=token create -d virtualbox default`
3. Get ip of the docker-machine: `docker-machine ip default`

- Docker compose
1. Install docker compose
* Linux:
`sudo curl -L https://github.com/docker/compose/releases/download/1.20.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose`
* Windows:
`[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12`
`Invoke-WebRequest "https://github.com/docker/compose/releases/download/1.8.0/docker-compose-Windows-x86_64.exe" -UseBasicParsing -OutFile $Env:ProgramFiles\docker\docker-compose.exe`
2. Up docker compose
`docker-compose up`
* Linux : visit 'http://0.0.0.0:4000'
* Windows: visit 'http://{docker-machine ip default}:4000'


- Run Docker
1. Change directory and run `docker build -t monefy .`
2. Run `docker run -p 4000:80 monefy`

# Telegram
Telegram Bot:
name - MonefyBot

# PostgreSQL
1. `sudo -u postgres psql`
2. \password postgres
3. `CREATE DATABASE monefy;`

# Alembic
1. `alembic init --template generic alembic`
2. change sqlalchemy.url in alembic.ini
3. `alembic current`
4. `import os
import sys
MODEL_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
sys.path.append(MODEL_PATH)
from db import transaction`
5. `target_metadata = transaction.Base.metadata`
6. Run `alembic revision --autogenerate -m "initial"`
