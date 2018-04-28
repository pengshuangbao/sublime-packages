# sublime-packages

使用git同步subl配置和插件

```
cd [package folder]/User
git init
```

# 以下文件不需要同步，添加至.gitignore文件：

```
Package Control.last-run
Package Control.ca-list
Package Control.ca-bundle
Package Control.system-ca-bundle
Package Control.cache/
Package Control.ca-certs/
encoding_cache.json
```

提交到远程仓库（如：github）

```
git add --all
git commit -m "your commit content"
git remote add origin [your git repository]
git push origin master
```

其它设备同步配置

```
cd [packages folder]
cp [packages folder]/User [package folser]/User_old
git clone [your git repository] User
```
