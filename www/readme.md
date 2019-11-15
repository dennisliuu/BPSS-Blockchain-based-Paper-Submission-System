# BPSS System

app.js: 負責啟動整個系統，檔案上傳的過程也在這裡處理
```nodejs
node app.js
```

routes/index.js: 網頁後端程式，操作 DB 與決定要傳什麼資料給前端

utils/checkDirExist.js: 檢查目前文件上傳時，存放文件的資料夾是否存在，若不存在則建立一個資料夾

utils/getUploadDirName.js: 建立名稱為日期的資料夾

utils/sendMail.py: 寄信

views/index.html: 前端頁面
