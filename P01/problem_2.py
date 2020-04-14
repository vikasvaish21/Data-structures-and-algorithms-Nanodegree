import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if suffix == "":
        return []
    
    if len(os.listdir(path)) == 0:
        return []

    path_elements = os.listdir(path)
    path_list = []
    if(os.path.exists(path)):
        for file in path_elements:
            full_path = path + '/' + file
            if os.path.isdir(full_path):
                path_list = path_list + find_files(suffix, full_path)
            else:
                if(file.endswith(suffix)):
                    path_list.append(full_path)
        return path_list


# Testing preparation
path_base = './testdir'

# Normal Cases:
print(find_files(suffix='.c', path=path_base))
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print(find_files(suffix='.h', path=path_base))
#['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h'] 

print(find_files(suffix='.z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# []
print(find_files(suffix='b.c', path=path_base))
# ['./testdir/subdir3/subsubdir1/b.c']
print ("./a.h".endswith(".h"))
# True
