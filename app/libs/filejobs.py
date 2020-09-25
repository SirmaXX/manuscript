import os
from git import Repo


COMMITS_TO_PRINT = 5

"""
dosya işlemleri
"""
def DeleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")


def FileOpen(filename):
    f = open(filename, "r")
    f.close()


def WriteFile(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()
    # open and read the file after the appending:
    return FileOpen(filename)


def CreateFile(filename):
     if os.path.exists(filename):
       print("dosya var")
     else:
        f = open(filename, "x")
        print("dosya oluşturuldu")
        f.close()

def EditFile(filename,text):
    f = open(filename, "a")
    f.write(text)
    f.close()
    # open and read the file after the appending:
    return FileOpen(filename)

def ListFiles(path):
    dirs = os.listdir( path )
   # This would print all the files and directories
    for file in dirs:
       print (file)

"""
git işlemleri
"""

def print_repository(repo):
    print('Repo description: {}'.format(repo.description))
    print('Repo active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))


def print_commit(commit):
    print('----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary,
                                     commit.author.name,
                                     commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(),
                                              commit.size)))