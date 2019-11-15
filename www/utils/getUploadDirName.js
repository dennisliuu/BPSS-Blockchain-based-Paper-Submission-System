const getUploadDirName = () => {
  const date = new Date()
  let month = Number.parseInt(date.getMonth()) + 1
  let day = date.getDate()
  month = month.toString().length > 1 ? month : `0${month}`
  day = day.toString().length > 1 ? day : `0${day}`
  const dir = `${date.getFullYear()}${month}${day}`
  return dir
}

module.exports = getUploadDirName
