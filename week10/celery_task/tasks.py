from celery import Celery
import pdfkit
import uuid
from sys import argv

import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from db_models import PDF


engine = create_engine('sqlite:///pdfs.db')

session = sessionmaker(bind=engine)
s = session()
app = Celery('tasks', broker='amqp://localhost')

COMMANDS = ('download', 'check')


@app.task
def make_pdf(url, filename):
    pdfkit.from_url(url, '{}.pdf'.format(filename))


def search_file(uuid):
    return s.query(PDF).filter(PDF.uuid==uuid).one()


def main():
    identifier = uuid.uuid4()
    if argv[1] in COMMANDS:
        if argv[1] == COMMANDS[0]:
            make_pdf.delay(argv[2], argv[2].split('.')[0])
            print("PDF for {} will be generated. Check with this UUID: {}".format(argv[2], identifier))
            pdf = PDF(uuid=str(identifier), url=argv[2], path=str(os.path.join(os.getcwd(), '{}.pdf'.format(argv[2].split('.')[0]))))
            s.add(pdf)
            s.commit()
        if argv[1] == COMMANDS[1]:
            path = search_file(argv[2])
            print("PDF for {} is located in {}".format(path.url, path.path))
    else:
        print("cmd ERROR")


if __name__ == '__main__':
    main()
