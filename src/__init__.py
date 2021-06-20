# TODO work on the doc string for the module when all finished
from src import deidentify_data



__doc__ = """
deidentify_data - Sythetic data generator library for Python
============================================================

**deidentify_data** is a python package providing a way to create synthetic
data to be used for non-production environments for testing applications.

Process
-------
 The synthetic data is based off of the real data and is designed to mimick the original
data as much as possible (and to even hopefully have all the same misgivings as the
 original). The process involves creating a profile of the original data that will 
 make note of datatypes, distributions, column content (like is a column of strings 
 uuids, names, geographic locations etc. ), and format of the content. The second step 
 of the process involves using the data profile to create a synthetic clone of the 
 original data to whatever specifications the user needs (for example, how many rows 
 or how many megabytes of data)
 
 Main Features
 -------------
 
"""