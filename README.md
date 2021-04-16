# Longest Strand
Given a large number of binary files, write a program that finds the
longest strand of bytes that is identical between two or more files

Use the test set attached (files sample.*)

The program should display:
- the length of the strand
- the file names where the largest strand appears
- the offset where the strand appears in each file

# Method
The longest common substrings of a set of strings can be found by building a generalized suffix tree for the strings, and then finding the deepest internal nodes which have leaf nodes from all the strings in the subtree below it.
