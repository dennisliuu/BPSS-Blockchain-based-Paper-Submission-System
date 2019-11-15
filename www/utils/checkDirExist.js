const path = require('path');
const fs = require('fs');

const checkDirExist = p => {
  if (!fs.existsSync(p)) {
    fs.mkdirSync(p);
  }
}

module.exports = checkDirExist
