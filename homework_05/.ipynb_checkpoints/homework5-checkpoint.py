# 3.1 Vocabulary review
#     1. Git is a software that is able to track and save changes made to you code to an remote repository, while Github is a platform for storing and sharing codd through repsotories created by indivisuals.
#     2. The termianl is the interfance between the user and the computer where hte user is able to create and edit code, while the commandline is the input line on the terminal where managing and creating code is done on.
#     3. a local repository exists locally on one's device, while a remote repository exits in the cloud, not not directly in the user's computer.
#     4. Version control is a system for tracking cahnges made to code by the user.
#     5. The stagaing area is entered right before changes are committed to github. the git add input is used, and afterwards any last minute changes that need to be made can be done just before the final commit.
#     6. git add indicates that the new changes made to the code are going to be added your code on git hub, this command allows oyu to enter the staging area and make any other last minute changes before commiting all new materials. 
#     7. git commit send the new changes to the git hub repository, all changes are then finalized.
#     8. git push pushed any changes and the local repository into the remote repository.
#     9. git staus shows the status of saved or unsaved changes and local repositories in git folders
#     10. git pull pulls changes, files and repositories from remote repositories to local repositories.
#     11. pwd shows the pathway taken to get from the root directory (on personal devices the User directory) to the current working directory.
#     12. ls lists all of the current directories and files within the current working directory.
#     13. cd allows the user to change directories, either to one within the current directory by using the directorie's name after cd, or followed by " .." to move one directory back.
#     14. nano allows the user to edit python files in the terminal.
#     15. touch is used to create a python ".py" file in the terminal.
#     16. mv allows one to move a directory or file to a new location in the local directories.
#     17. rm allows for a file or directory to be removed from the computer.
#     18. cat concatinates/ displays a file's content on the terminal.

# 3.2 Directory Tree
#     The pwd command will display the pathway and the final entry will be the working directory
#     ls will show all files and directories within your current one, ls -a will also display hidden files.
#     cd .. will allows you to move back one directory, to where you can ls and file brianna_repo and cd to change into brianna_repo as the current directory. The commands git fetch and git pull will be able to pull new files and chnges from the remote repsository to the local if all changes are saved on the local repository.
#     mv homework.py homework/
#     Use cd .. to reenter the parent depository for judy_decal/ and brainna_repo and cd into judy_decal_ and subsequently cd into the homework/ folder.
#     homework.py is a file, therefore the command nano can be used to open the file to an editable area, and you can call python3 homework.py to run the file fro mthe commandline (only displaying outputs).
#     git add will dispaly all of the changes made to your file in a git-monitored folder, once any last minute cahgnes are made the git commit command will save all changes to the git repository.
#     change's/ code that exists on the remote repository does not exists on the local repository currently being pushed. To finish pushing the changes you want to, the remote respository firest ahs to be fetched andthe local respoitroy updated, so the repositories match before commiting new changes.
#     ~/ / Recent/ , or from the current homework directory --> homework/ / judy_decal/ / python_decal/ / ~/ / Recent/

# 4.1 Homework 3 Review
def checkDataType(x):
    return type(x)

#def checkDataType(x):
    #return type(x)

#checkDataType(3.14)
#checkDataType(True)

def evenOrOdd (x):
    if x%2 == 0:
        return (True)
    else:
        return (False)
#evenOrOdd(7)
#evenOrOdd(10)

def sumWithLoop(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
#sumWithLoop([1,2,3,4,5])

def duplicateList(numbers):
    newList = []
    for i in numbers:
        newList.append(i)
        newList.append(i)
    return newList
#duplicateList(["a","b","c"])

#def square(num)
    #return num * num 
# colon is missing from the defenition line, following code will not be including in function defenition and will produce an error.

def square(num):
    return (num*num)

# favorite function

def favoriteFunction(numbers):
    print(f "The function duplicateList() takes the input {numbers} and returns {duplicateList(numbers)}")

#favoriteFunction([1,2,3,4,5])
