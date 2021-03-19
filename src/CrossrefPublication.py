# -*- coding: utf-8 -*-
'''
Created on 22 feb. 2021

@author: reinaqu_2
'''
from dataclasses import dataclass
from typing import TypeVar, List, Set, Dict, Optional, Any
import crossref_commons.retrieval
import crossref_commons.relations
import Preconditions
import json


CrossrefPublication = TypeVar('CrossrefPublication')
@dataclass(frozen=True)
class CrossrefPublication:
    doi:str=None
    json: Dict[str, Any]=None
    
    @staticmethod   
    def of(doi:str) -> CrossrefPublication:
        js=crossref_commons.retrieval.get_publication_as_json(doi)
        Preconditions.checkArgument(js, 'doi not found')
        return CrossrefPublication(doi, js)
        
    @property
    def get_title (self)->str:
        title_list = self.json.get("title", None)#
        if len(title_list)>0:
            title = title_list[0]
        else:
            title=None
        return title
    
    @property
    def get_doi (self)->str:
        return self.doi
    
    @property
    def get_references (self)->List[Any]:
        return self.json.get("reference",[])
    @property
    def get_abstract(self)-> str:
        return self.json.get("abstract","")
    
    @property
    def get_references_dois(self)->List[str]:
        dois=[]
        for reference in self.get_references:
            doi = reference.get("DOI", None)
            if doi != None:
                dois.append(doi)
        return dois
    
    @property
    def get_references_without_dois(self)->List[Any]:
        refs=[]
        for indx, reference in enumerate(self.get_references):
            doi = reference.get("DOI", None)
            if doi == None:
                unstr = reference.get("unstructured")
                refs.append((indx+1,unstr))
        return refs
    

if __name__ == '__main__':
    cp = CrossrefPublication.of('10.1007/978-3-642-11996-5_18')
    print (cp.get_title)
    print(cp.get_doi)
    print(cp.json)
    dois = cp.get_references_dois
    print(dois)
    no_dois=cp.get_references_without_dois
    for r in no_dois:
        print (r)
    print("number of dois ", len(dois))
    print("number of no dois ", len(no_dois))    
    
    