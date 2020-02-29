#  git基本操作（我已经忘了，自己找回）

1. git init 初始化

2. git status    状态:  （红色代表修改过但是没有在暂存区， 绿色表示在暂存区）

3. git add file_name
添加到暂存区

4. git commit -m '第一次提交代码'
提交到版本库

5. git log   
查看提交历史

6. git reset --hard  版本号 回滚代码， 新代码会被删除

7. git reset --soft 版本号 回滚代码， 新代码会不被删除

8. git push orgin master 
提交到远程仓库



# 分支

1. 查看分支

```bash
git branch
```


2。新建分支


```bash
git branch name
```




3. 切换分支


```bash
git checkout name或者-
```



4. 合并代码

```bash
git merge  name 
```
5. 只可以将新修改的代码合并到老代码上，不可以将老代码合并到新的上





## git ignore

http://gitbook.liuhui998.com/4_1.html