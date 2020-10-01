docker build -t scraper:0.0 ./scraper
docker rm -f scraper
docker run -it --name scraper scraper:0.0