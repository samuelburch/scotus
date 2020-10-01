FROM python:3.6-slim

RUN apt-get -y update && apt-get install -y \
    git \
    gcc \
    libmariadb-dev

RUN pip install --upgrade pip && \
    pip install \
    twint \
    mariadb \
    schedule

#RUN pip install --user --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
        
COPY . .

CMD python scraper.py