#!/bin/zsh

# Run the docker build commant putting today's date and time as the tag
# Further, make sure to add the tag: latest

sudo docker build -t "jwmarcus/rainman:$(date +'%Y%m%d_%H%M')" -t jwmarcus/rainman:latest .

sudo docker push --all-tags jwmarcus/rainman