# Atlas 3.0 Backend

The tech stack used is Django with Django-Ninja package running on Python 3.12.

## Setup guide

1. Clone this repository
2. Download [Python 3.12](https://www.python.org/downloads/) and create a virtual environment by running
    ```shell
    python3.12 -m venv venv
    ```
3. Start the virtual environment

    On Unix/macOS
    ```shell
   source ./venv/bin/activate
    ```
   On Windows
    ```shell
   .\venv\Scripts\activate.bat
    ```
4. Install the required packages
   ```shell
   python -m pip install -r requirements.txt
   ```
5. Install [PostgresSQL](https://www.postgresql.org/download/) (can use the latest version or use version 14.0 which is the version used at the time of writing this guide)
6. Start pgAdmin
7. Connect to the local PSQL server and create a database `atlas_3`. Ensure encoding is UTF-8.
8. Change directory to `atlas_3`
   ```shell
   cd atlas_3
   ```
9. In root directory. Create a `.env` file with the following content:
    ```
    DB_USER=YOUR_DB_USERNAME (default postgres)
   DB_PASSWORD=YOUR_DB_PASSWORD (default postgres)
   DB_PORT=YOUR_DB_PORT (default 5432)
    ```
10. Run the migrations for the database
    ```shell
    python manage.py migrate
    ```
11. Start the server
    ```shell
    python manage.py runserver
    ```
