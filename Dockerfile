FROM selenium/standalone-chrome

WORKDIR ./

CMD ["sudo", "apt-get", "update"]

CMD ["cd", "home"]

CMD ["cd", "seluser"]

CMD ["sudo", "apt-get", "-y", "install", "git"]

CMD [ "git", "clone", "https://github.com/sachiniyer/delivery-service.git" ]

CMD ["cd", "delivery-service"]

CMD ["bin/bash", "install"]
