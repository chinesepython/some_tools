# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch


es_xnr = Elasticsearch(['192.168.169.45:9205','192.168.169.47:9205','192.168.169.47:9206'], timeout=600)
xnr_no = '  '

query_body = {
    'query':{
        'filtered':{
            'filter':{
                'bool':{
                    'must':[
                        {'term': {'xnr_no': xnr_no}}
                    ]
                }
            }
        }
    },
    'size': 999,
}
res = es_xnr.search('weibo_xnr_relations', 'user', query_body)['hits']['hits']
id_list = [item['_id'] for item in res]


for id in id_list:
    print es_xnr.delete(index='weibo_xnr_relations',doc_type='user',id=id)

