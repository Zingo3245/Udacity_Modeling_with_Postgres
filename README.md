# Data Modeling with Postgres

Project 1 for the Udacity data engineering nano degree involves a fictional company called Sparkify that wants to create a postgres database for their songs. This involves creating a python script that takes JSON data and loads it into the postgres database.

## Installation

Clone the github repo and use pip install to install the required libraries

``
git clone https://github.com/Zingo3245/Udacity_Modeling_with_Postgres
cd Udacity_Modeling_with_Postgres
pip install -r requirements.txt
``

## Usage

This project uses python scripts that can be run from the terminal:

``
python create_tables.py

python etl.py
``

To make sure this runs correctly you will need to have postgres with the sparkify database set up with a user name and a password.

## License

This project is distributed under the GPL 3.0 license.