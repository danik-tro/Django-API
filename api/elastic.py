from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
import json


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


def elastic_test_1():
    el_db = ElasticSearchDB()

    print(el_db.create_index('test', 'test-doc', 1, {
        'test': 'test',
        'fieldsArray': [
            {'test_1': "test2"},
            {'test_2': "test3"},
            {'test_3': "test4"}
        ],
    }))

    print(el_db.get('test', 'test-doc', 1))
    print(el_db.delete_item('test', 'test-doc', 1))
    print(el_db.delete_index('test'))


def elastic_test_2():
    import random

    bodies = [{
        "name": f"name_{i}",
        "field": f'field_{i}',
        "fields": [f'field_{random.randint(0, 100)}' for j in range(10)]
    } for i in range(50)]

    es = ElasticSearchDB()

    for index, body in enumerate(bodies, 1):
        es.create_index(index='test',
                        doc_type='test-doc',
                        id_=index,
                        body=body)

    print(es.get_mapping('test'))

    for index in range(1, len(bodies)+1):
        es.delete_item(index='test',
                       doc_type='test-doc',
                       id_=index)


if __name__ == "__main__":
    elastic_test_2()
