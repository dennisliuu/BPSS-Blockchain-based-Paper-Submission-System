const path = require('path');
const koa = require('koa');
const nunjucks = require('koa-nunjucks-2');
const koaBody = require('koa-body');
const router = require('./routes');

const checkDirExist = require('./utils/checkDirExist');
const getUploadDirName = require('./utils/getUploadDirName');

const cors = require('@koa/cors');

const app = new koa();
app.use(cors());

app.use(nunjucks({
  ext: 'html',
  path: path.join(__dirname, './views'),
  nunjucksConfig: {
    trimBlocks: true
  }
}));

app.use(koaBody({
  multipart: true,
  encoding: 'gzip',
  formidable: {
    uploadDir: path.join(__dirname, 'public/upload'),
    keepExtensions: true,
    // maxFieldsSize: 2 * 1024 * 1024,
    onFileBegin: (name, file) => {
      console.log(file);
      const dirName = getUploadDirName();
      const dir = path.join(__dirname, `public/upload/${dirName}`);
      checkDirExist(dir);
      const fileName = file.name;
      file.path = `${dir}/${fileName}`;
      app.context.uploadpath = app.context.uploadpath ? app.context.uploadpath : {};
      app.context.uploadpath[name] = `${dirName}/${fileName}`;
      
      const { spawn } = require('child_process');
      const pyProg = spawn('python', ['./utils/sendMail.py']);
      pyProg.stdout.on('res', function(res) {
          console.log(res.toString());
      })

    },
  }
}));
app.use(router.routes()).use(router.allowedMethods());


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log('[ok] Server starts at http://127.0.0.1:3000');
});

