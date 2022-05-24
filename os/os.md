# os

## Outline

&emsp; os套件為Python**內建套件**，不需要額外安裝。

&emsp; 引入方法為:

```Python
    import os
```

&emsp; 我目前最常用來進行:

* 改檔名
* 確認檔案或路徑存在
* 確認和更改使用者執行路徑
* 獲得路徑下資料清單
* 創建新目錄
* 刪除檔案
* 使用cmd指令
  
## Menu

1. [改檔名](#rename)
2. [確認檔案或目錄存在](#path)
3. [確認和更改使用者執行路徑](#chdir)
4. [獲得路徑下資料清單](#listdir)
5. [創建新目錄](#mkdir)
6. [刪除檔案](#remove)
7. [使用cmd指令](#system)

## rename

&emsp;第一個常用功能就是改檔名，使用方法也非常簡單。

```Python
    os.rename('舊檔名(含路徑)','新檔名(含路徑)')
```
&emsp;切記: 一定要記得加上路徑

&emsp; [回目錄](#Menu)

## path

&emsp;第二個常用功能就是確認檔案或目錄存在，函數都在os.path下

```Python
    os.path.isdir(input) #檢查input是否為目錄 return bool
    os.path.isfile(input) #檢查input是否為檔案 return bool
```

&emsp; [回目錄](#Menu)

## chdir

&emsp;第三個常用功能就是修改執行目錄，避免使用相對路徑找不到目標檔案。

&emsp;常和getcwd()一起用。

```Python
    os.getcwd() #獲的當前執行路徑 return str
    os.chdir(path) #將執行路徑改為path
```

&emsp; [回目錄](#Menu)

## listdir

&emsp;第四個常用功能就是獲得輸入目錄下，下層的所有檔案。

```Python
    os.listdir(path) #將path下一層所有檔案和目錄寫成一個list retuen list
```

&emsp; [回目錄](#Menu)

## mkdir

&emsp;第五個常用功能就是建立一個新目錄。

```Python
    os.mkdir((path+)name) #新增一個name資料夾於path處
```

&emsp; [回目錄](#Menu)

## remove

&emsp;第六個常用功能就是刪除檔案和**空資料夾**。

```Python
    os.remove(path+target) #刪除path下target檔案或空資料夾
```

&emsp; [回目錄](#Menu)

## system

&emsp;第七個常用功能就是執行cmd指令。

&emsp;非常好用。如果要呼叫其他檔案都可以使用。

```Python
    os.system(command) #執行command(str)指令
    os.system('pause') #按一下繼續(Windows用)
    os.system('cls') #清除cmd(Windows用)
    os.system('clear') #清除cmd(linux用)
```

&emsp; [回目錄](#Menu)

## 更新日期

2022/05/24