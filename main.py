# -*- coding: utf-8 -*-
"""
In quale periodo dell'anno i taxi vengono utilizzati di più? Creare un file di risultati e
 un grafico che, per ogni mese, indichi il numero medio di viaggi registrati ogni giorno. 
 A causa delle differenze tra le zone di New York, vogliamo visualizzare le stesse 
 informazioni per ogni borough. Notate qualche differenza tra di loro? Qual è il mese 
 """
from lettura_file import leggi_file

percorsoFile = input("dammi il percoso del file .parquet da leggere: ")

data_taxi=leggi_file.leggi_file_parquet(percorsoFile)

  

        






















#lettura_file.percorsoFile(percorsoFile)
#dataTaxi=lettura_file.lettura_file_parquet(percorsoFile)

#if __name__=='main':
#data= pd.read_parquet('C:/Users/antos/Desktop/python/Python Scripts/GitHub/progetto1/dataTaxi/yellow_tripdata_2022-01.parquet')
    
    
#


