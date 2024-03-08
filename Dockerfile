FROM python:latest

# Update aptitude with new repo
RUN apt-get update

# Install software
RUN apt-get install -y git

# Clone repo
RUN git clone https://github.com/qloridant/observatoire_produits

# Install requirements
RUN cd observatoire_produits && pip install -r requirements.txt

# Import environnement variables
COPY .env observatoire_produits/.env

# RUN
CMD  ["python", "observatoire_produits/src/data/make_dataset.py"]
