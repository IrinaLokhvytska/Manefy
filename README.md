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

- Run Docker   
1. Change directory and run `docker build -t monefy .`
2. Run `docker run -p 4000:8000 monefy`

# Telegram
Telegram Bot:
name - MonefyBot
username - monefy_bot
key - 567099147:AAFXaoHQGtTiDFeehr3UbfpQrTs9FPssjyw
