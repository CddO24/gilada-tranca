def suma(*num):
    return sum(num)

print(suma(2,4,33,121,23,2,1,2))
"""$ python d:/repos/fun.py
4

Usuario@DESKTOP-6JGHB8G MINGW64 /d/repos (master)
$ git add func.py
fatal: pathspec 'func.py' did not match any files

Usuario@DESKTOP-6JGHB8G MINGW64 /d/repos (master)
$ git add fun.py

Usuario@DESKTOP-6JGHB8G MINGW64 /d/repos (master)
$ git commit -m "funcion-suma"
[master (root-commit) d3ebda9] funcion-suma
 1 file changed, 11 insertions(+)
 create mode 100644 fun.py

 $ git switch -c optimize-sum-function
Switched to a new branch 'optimize-sum-function'

Usuario@DESKTOP-6JGHB8G MINGW64 /d/repos (optimize-sum-function)
$ git branch
  master
* optimize-sum-function
"""



