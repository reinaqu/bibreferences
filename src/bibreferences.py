# -*- coding: utf-8 -*-
"""
The result is a set of statistics about the file given as a parameter.

A. M. Reina Quintero <reinaqu@us.es>

"""
import argparse
from bibtexparser.bibdatabase import BibDatabase
import bibtexparser
from bibtexparser.bparser import BibTexParser
import os.path
from bibutils import *
import logging
from CrossrefPublication import *
from conversions import *
from dois import *

def main():
    
    logging.basicConfig(level=logging.INFO)
    args = parse_arg()
    
    doi = args.doi[0]  #Obtain the doi of interest from args
    print("References for doi", doi)
    
    filename = doi+".bib"  #Generate the bibtex filename used as output
    if args.output:
        filename = args.output        

    cp = CrossrefPublication.of(doi)  #Obtain the publication data from crossref
    
    if cp.get_abstract!="": ## Just to test if the publication has the abstract field
        logging.info(doi+ " has abstract")
        
    bibdb = crreferences2BibtexEntries(cp) #Generate list of bibtex entries for the referenced publications with doi
    dois_num = len(bibdb.get_entry_list()) #Calculate the number of referenced publications with doi
    write_bibtex(bibdb, filename) #write the bibtex entries to a bibtex file
    
    no_dois=cp.get_references_without_dois #Generate the list of referenced publications without doi
    no_dois_num = len(no_dois) #Calculate the number of referenced publications without doi
    for indx, r in no_dois:
        if r != None:
            print ("({},{})".format(indx, r.encode('cp1252', errors='replace').decode('cp1252')))
        else:    
            print ("({},)".format(indx))
    print("number of dois ", dois_num)
    print("number of no dois ", no_dois_num)
    num_references = dois_num+no_dois_num
    percentage=None
    if num_references>0:
        percentage = 100* no_dois_num/num_references
    print ("no dois percentage", percentage)    
  
 

def parse_arg():
    #parse args
    parser = argparse.ArgumentParser(prog='bibreferences', description='Bibtex with references')
    parser.add_argument('-doi', nargs=1, type=str)
    parser.add_argument('-o', '--output', nargs='?', help='file')
    return parser.parse_args()

if __name__ == "__main__":
    main()