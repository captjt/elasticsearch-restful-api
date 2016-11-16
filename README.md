# elasticsearch-restful-api

This is a small [_Flask_](http://flask.pocoo.org/) RESTful API that uses
* [Flask-RESTful](http://flask-restful.readthedocs.io/en/0.3.5/)
* [Elasticsearch](https://www.elastic.co/products/elasticsearch)

The data set I have in the Elasticsearch server comes from @danielfrg's [repo](https://github.com/danielfrg/espn-nba-scrapy/tree/master/data)

I configured my own ingestion [application](https://github.com/jtaylor32/elasticsearch-bulk-ingestion) to ingest the data sets.

## Running the application

    Requirements
        Python 3.5+
        Elasticsearch 2.x
 
 1. Clone the repository
 2. `pyvenv env`
 3. `source env/bin/activate`
 4. `pip install -r requirements.txt`
 4. Turn on your elasticsearch server (defaults to port 9200)
    * In your elasticsearch directory `bin/elasticsearch`
 5. Configure the `extensions.py` to point to your elasticsearch server's address
    * Or set the `ELASTICSEARCH_URL` environment variable to your address
 6. `python manage.py runserver`