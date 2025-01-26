from dotenv import load_dotenv
import os
from database.main import db
from config import conf


def main():
    db.set_config(conf)
    db.create_all()
    load_dotenv(os.path.join(os.getcwd(), '.env'))


if __name__ == '__main__':
    main()
