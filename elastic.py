import pandas as pd
import numpy as np
import streamlit as st
import eland as ed
from elasticsearch import Elasticsearch

class elastickiva:
    es = None
    cloud_id ="enterprise-search-deployment:ZWFzdHVzMi5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDdmMzBjYjUzMzQxOTRjYTM5YjVkMDE0NGExMWM1NjZkJGY5NDI3N2JmZmVkMjQ1MzA4NGI2Mjk0MGFmMGE4NWE3"
    username ="elastic"
    password ="06QgnsL0FNg2SZ8J7PYgzRkv"
    indexname = "*kiva-loans*"
    df = None
    

def get_df():
    ek = elastickiva()
    ek.es = Elasticsearch(
    cloud_id=ek.cloud_id,
    http_auth=(ek.username, ek.password))
    idx_list = [x for x in (ek.es).indices.get_alias(ek.indexname).keys() ]
    ek.df = ed.DataFrame(ek.es, es_index_pattern=idx_list[0])
    return(ek)













