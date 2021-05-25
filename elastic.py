import pandas as pd
import numpy as np
import streamlit as st
import eland as ed
from elasticsearch import Elasticsearch

class elastickiva_con:
    es = None
    cloud_id ="enterprise-search-deployment:ZWFzdHVzMi5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDdmMzBjYjUzMzQxOTRjYTM5YjVkMDE0NGExMWM1NjZkJGY5NDI3N2JmZmVkMjQ1MzA4NGI2Mjk0MGFmMGE4NWE3"
    username ="elastic"
    password ="06QgnsL0FNg2SZ8J7PYgzRkv"
    indexname = "*kiva-loans*"
    indexname_actual = ""

class elastickiva:
    df = None
    
@st.cache(allow_output_mutation=True)
def get_conn():
    ekcon = elastickiva_con()
    ekcon.es = Elasticsearch(
    cloud_id=ekcon.cloud_id,
    http_auth=(ekcon.username, ekcon.password))
    idx_list = [x for x in (ekcon.es).indices.get_alias(ekcon.indexname).keys() ]
    ekcon.indexname_actual =idx_list[0]
    return(ekcon)


def get_df():
    ek = elastickiva()
    ek_con = get_conn()
    ek.df = ed.DataFrame(ek_con.es, 
    es_index_pattern=ek_con.indexname_actual)
    return(ek)












