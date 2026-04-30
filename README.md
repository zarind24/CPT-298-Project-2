# Maine Towns ETL Project

**About:**

This project loads Maine towns data into a PostgreSQL warehouse.

**The program does 3 steps:**

1. Gets the data from the Maine ArcGIS website
2. Cleans and formats the data
3. Loads the data into PostgreSQL

It can also run automatically using cron.

**## Tools Used**

* Python
* PostgreSQL
* Pandas
* Requests
* VS Code

**## Files**


src/        Python files
config/     Database settings
sql/        SQL table file
requirements.txt
README.md


**## How to Run**
Create virtual environment:


python3 -m venv .venv
source .venv/bin/activate


Install packages:


pip install -r requirements.txt


Run project:


python -m src.main


**## Automation**

Example cron job:


0 2 * * * cd /path/to/project && python3 -m src.main


**This runs every day at 2:00 AM.**

**## Authors**

Created by Zarin Deane and Hayden Allen

