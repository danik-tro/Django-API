from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q, Text, Integer, Document, Long
from elasticsearch.helpers import bulk


class BookDoc(Document):
    title = Text
    url = Text
    author = Text
    price = Text
    code = Long
    id = Long

    class Index:
        name = 'books'


class ElasticSearchDB:
    def __init__(self, host='localhost', port=9200):
        self.es = Elasticsearch([{
            "host": host,
            "port": port,
        }])

    def delete_item(self, index, doc_type, id_):
        return self.es.delete(index=index,
                              doc_type=doc_type,
                              id=id_)

    def delete_index(self, index):
        return self.es.indices.delete(index=index,
                                      ignore=[400, 404])

    def create_index(self, index, doc_type, id_, body):
        return self.es.index(
            index=index,
            doc_type=doc_type,
            id=id_,
            body=body
        )

    def get_mapping(self, index):
        return self.es.indices.get_mapping(index=index)

    def get(self, index, doc_type, id_):
        return self.es.get(index=index,
                           doc_type=doc_type,
                           id=id_)


class BookElasticSearchDB(ElasticSearchDB):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_documents(self, data):
        for category in data:
            if not category:
                continue

            bulk(self.es,
                 [{**BookDoc(**item).to_dict(include_meta=True), **{'_type':'BookDoc'}} for item in category],
                 index='books', doc_type='BookDoc')

