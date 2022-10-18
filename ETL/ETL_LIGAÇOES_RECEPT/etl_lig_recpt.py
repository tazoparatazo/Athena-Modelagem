# -*- coding: utf-8 -*-
"""ETL_LIG_RECPT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j1NEyntsBU7Q0hQj-hP_lELZJTfFxMgK

#**. Executar Extração**

##**. Instalação**
"""

# @title Instalação
!pip install pandas
!pip install gcsfs

"""##**. Setup**"""

# @title Setup

from google.colab import auth
from google.cloud import bigquery
from google.colab import data_table
from google.cloud import storage
import pandas as pd
import os

project = 'athenas-364914' 
location = 'US' 
client = bigquery.Client(project=project, location=location)
data_table.enable_dataframe_formatter()
auth.authenticate_user()

"""##**. Visualização de Querry**"""

# @title SQL de consulta

job = client.get_job('bquxjob_6f8a23e9_183c3bd4c53') 
print(job.query)

"""##**. Visualização de Dados**"""

# @title Visualização

job = client.get_job('bquxjob_6f8a23e9_183c3bd4c53') 
results = job.to_dataframe()
results

"""extração

##**. Extração dos Dados**
"""

# @title Extração

df = results
df.to_excel('/content/ligacoes_recep.xlsx', index = False)

"""##**. Conexão ao GCP**"""

# @title Conexão ao GCP

serviceAccount = '/content/athenas-364914-4e16df1244dc.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = serviceAccount

"""##**. Inserindo Excell no GCP**"""

# @title Inserindo Excell no GCP


client = storage.Client.from_service_account_json(json_credentials_path='/content/athenas-364914-4e16df1244dc.json')
bucket = client.get_bucket('saida_modelagem')
object_name_in_gcs_bucket = bucket.blob('ligacoes_recep.xlsx')
object_name_in_gcs_bucket.upload_from_filename('ligacoes_recep.xlsx')