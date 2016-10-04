from git import Repo, Actor
import shutil
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
repo_dir = os.path.join(script_dir, 'test-git-repo')

try:
    shutil.rmtree(repo_dir)
except OSError:
    # Ignore repo dir does not exist error
    pass

os.mkdir(repo_dir)

git_repo = Repo.init(repo_dir)

test_file_name = os.path.join(repo_dir, 'test.txt')

with open(test_file_name, 'w') as test_file:
    test_file.write('test\n')

print(git_repo.active_branch)
assert not git_repo.is_dirty()
print(git_repo.untracked_files)

git_repo.index.add(['test.txt'])
assert git_repo.is_dirty()
print(git_repo.untracked_files)

committer = Actor("Michel Lampo", "michel@creatingfuture.eu" )

git_repo.index.commit('Initial commit', committer=committer)

with open(test_file_name, 'a') as test_file:
    test_file.write('Git just works\n')

git_repo.index.add(['test.txt'])
assert git_repo.is_dirty()
print(git_repo.untracked_files)

git_repo.index.commit('Added git info', committer=committer)

with open(test_file_name, 'a') as test_file:
    test_file.write('But it can be a bit touchy\n')

git_repo.index.add(['test.txt'])
assert git_repo.is_dirty()
print(git_repo.untracked_files)

git_repo.index.commit('Added warning', committer=committer)

# Find history of a given file
commits_touching_path = list(git_repo.iter_commits(paths=[test_file_name]))


for commit in commits_touching_path:
    print(commit)
    # Do not use the full path here, only the one relative to the git repo location!!!
    print((commit.tree / 'test.txt').data_stream.read())


# Or  retrieving commits and commits in one go
revlist = (
    (commit, (commit.tree / 'test.txt').data_stream.read())
    for commit in git_repo.iter_commits(paths=test_file_name)
)


for commit, filecontents in revlist:
    print(commit)
    print(filecontents)
