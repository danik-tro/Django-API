from elasticsearch import Elasticsearch
import json


class ElasticSearchDB:
    def __init__(self, host='localhost', port=9200):
        self.es = Elasticsearch([{
            "host": host,
            "port": port,
        }])

    def delete_item(self, index, doc_type, id_):
        print(self.es.delete(index=index,
                             doc_type=doc_type,
                             id=id_))

    def delete_index(self, index):
        self.es.indices.delete(index=index,
                               ignore=[400, 404])

    def create_index(self, index, doc_type, id_, body):
        print(self.es.index(
            index=index,
            doc_type=doc_type,
            id=id_,
            body=body
        ))

    def get(self, index, doc_type, id_):
        self.es.get(index=index,
                    doc_type=doc_type,
                    id=id_)


if __name__ == "__main__":
    el_db = ElasticSearchDB()

    el_db.create_index('test', 'test-doc', 1, {
        'test': 'test',
        'fieldsArray': [
            {'test_1': "test2"},
            {'test_2': "test3"},
            {'test_3': "test4"}
        ],
    })

    el_db.get('test', 'test-doc', 1)

    el_db.delete_item('test', 'test-doc', 1)

    el_db.delete_index('test')


