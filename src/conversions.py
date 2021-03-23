# -*- coding: utf-8 -*-
'''
Created on 22 feb. 2021

@author: reinaqu_2
'''
from CrossrefPublication import *
#from Publication import *
from bibtexparser.bibdatabase import BibDatabase
from dois import *
from typing import Dict, Any
import time
# def crossRef2Publication(crpub:CrossrefPublication)->Publication:
#     
#     return Publication.of(crpub.get_doi, crpub.get_title, [], crpub.get_references_dois)


# def publication2BibtexEntry(pub:Publication)-> Dict[str, Any]:
#     e = get_bibtex_entry(pub.get_doi)
#     return e

# def references2BibtexEntries(pub:Publication)-> List[Any]:
#     
#     entries = [get_bibtex_entry(doi) for doi in pub.references_dois]
#     return entries    

def crreferences2BibtexEntries(crpub:CrossrefPublication)-> BibDatabase:
    
    entries=[]
    for doi in crpub.get_references_dois:
        entries.append(get_bibtex_entry(doi))
        time.sleep(2)
    return entries_to_bibdb(entries)    

if __name__=="__main__":
    
    cp = CrossrefPublication.of('10.1145/2675743.2771826')
    entries = crreferences2BibtexEntries(cp)
#     pub = crossRef2Publication(cp)   
#     entries = references2BibtexEntries(pub)
    print(entries_to_str(entries))
