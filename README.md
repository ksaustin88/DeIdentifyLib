# deidentify_data

# Vision

Application developers need to develop in an unencombered environment  where they are allowed to make mistakes, accidentally overwrite
or expose data and so forth. Thus many are using de-identified data or synthetic data to test out the functionality of
incremental additions to their codebase. However, getting really good synthetic data that matches the given nuances of the original
is a tough problem. It does happen that a given pathological behavior in the real data does not match anything experienced with the
synthetic data and therefore an application runs the risk of entering the next phase with a potential bug. The purpose of this library
is to provide automated data structure profiling and a data generation tool that can create synthetic data based on the profile of the
original data.

# Guide for developers

1. Firstly I want nothing by the most pythonic library here: Following the PEP 8 Style for python code as closely as possible (
see the following [link](https://www.python.org/dev/peps/pep-0008/) ).
2. Unit testing as we write.

# Pytest Guide

# Getting started with this library

# TODO

1. Create a profile class with three methods
   1. to_json: this should properly json serialize the class
   2. from_json: This should be able to convert a json serialized version of this profile object back to a profile
   3. merge: this should allow us to merge two profile objects
2. Create a JunkJson and JunkDataFrame classes where we can dynamically
create json or dataframe, resp., that has at least one representative of each kind
of case that our deidentification tool can (or should) recognize and profile.
3. Create a FullReader, RandomSampler, and a MinimalSampler that can read
all, random parts, and as little as possible of the data from the source to
be able to make a proper deidentification.
4. In the profiling, we should be able to recognize a wide variety of data
formats and also have a data writing tool that can additionally act on those formats
and write the deidentified data to file properly.
