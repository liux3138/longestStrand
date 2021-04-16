import suffix_trees
import pathlib


def longest_strand(*args):
    """
    Given a large number of binary files, this program can find the
    longest strand of bytes that is identical between two or more files
    using modified Generalized Suffix Tree library (https://github.com/ptrus/suffix-trees).

        input: the names of the binary files
        return:
            - the length of the strand
            - the file names where the largest strand appears
            - the offset where the strand appears in each file

    """

    file_dic = {}

    # Read through all files, covert bytes to characters and store them in a dictionary
    for file in args:
        for byte in pathlib.Path('data/' + file).read_bytes():
            file_dic[file] = file_dic.get(file, '') + chr(byte)

    # Build the Generalized Suffix Tree
    file_dic_list = list(file_dic.values())
    st = suffix_trees.STree(file_dic_list)
    longest_str, ids, offsets = st.lcs()

    print("The length of the longest strand of bytes is:", len(longest_str))

    # Compute the offset where the strand appears in each file
    file_names, iter_offsets = list(file_dic.keys()), iter(offsets)
    file_length = 0
    file_list = []

    for file_idx in ids:
        file = file_names[file_idx]
        file_list.append(file)

    for file in file_names:
        if file in file_list:
            print("The largest strand appears at", file,
                  "and the offset in bytes is", next(iter_offsets) - file_length)
        file_length += len(file_dic[file]) + 1


if __name__ == '__main__':
    longest_strand('sample.1', 'sample.2', 'sample.3', 'sample.4', 'sample.5',
                   'sample.6', 'sample.7', 'sample.8', 'sample.9', 'sample.10')
