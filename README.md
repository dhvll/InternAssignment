# InternAssignment
 Setting Multiple Database for different apps.
## Technologies

- Django
- Python

## Getting Started

To get a local copy up and running follow these simple steps:

### Prerequisites

- Python 3.

### Installation

1. Create a local copy of this git repository with `git clone` command.

   ```shell
   $ git clone https://github.com/dhavall13/InternAssignment.git
   ```

2. Create a Virtual Enviornment with the `virtualenv` module.

   ```shell
   $ virtualenv .
   ```

3. Once you’ve created a virtual environment, you may activate it.

   ```shell
   $ source Scripts/activate
   ```

4. Now, install the requirements from the `requirements.txt` file.

   ```shell
   $ pip install -r requirements.txt
   ```

5. Now, apply the migrations with the management command.

   ```shell
   $ python manage.py migrate --database=users_db (for users app)
   $ python manage.py migrate --database=products_db (for products app)
   ```
6. Now, create superuser

   ```shell
   $ python manage.py createsuperuser --database=users_db 
   ```

7. Finally, start the developement server with the management command.

   ```shell
   $ python manage.py runserver
   ```



## Authors

- Dhaval Chaudhari - *Initial work* - [dhaval](https://github.com/dhavall13)

