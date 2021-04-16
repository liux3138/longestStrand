# Longest Strand
Given a large number of binary files, write a program that finds the
longest strand of bytes that is identical between two or more files

Use the test set attached (files sample.*)

The program should display:
- the length of the strand
- the file names where the largest strand appears
- the offset where the strand appears in each file

# Method
The longest common substrings of a set of strings can be found by building a generalized suffix tree for the strings, and then finding the deepest internal nodes which have leaf nodes from all the strings in the subtree below it. (Sources: [Wikipedia: Longest common substring problem](https://en.wikipedia.org/wiki/Longest_common_substring_problem), [Suffix Tree Application 5 – Longest Common Substring](https://www.geeksforgeeks.org/suffix-tree-application-5-longest-common-substring-2/))

Before building the generalized suffix tree, I converted the binary files into strings of characters. Then, I modified the [generalized suffix tree library](https://github.com/ptrus/suffix-trees) to construct the Generalized Suffix Tree. The original library will find the longest common substring of all strings. But after being modified, it can find the the longest common substring between two or more files by finding the deepest node that was created by at least two files instead of all files. This algorithm takes linear time.

# Files
- main.py: The main file calls longest_strand.py which will build the generalized suffix tree based on the modified library "suffix-trees.py"
- suffix-trees.py: Python implementation of Generalized Suffix Trees.
- output.txt: This file contains the output after running "main.py"
