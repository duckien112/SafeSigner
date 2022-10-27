const puppeteer = require('puppeteer');
const fs = require('fs');
const readLastLines = require('read-last-lines');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto("https://cosmos.network/ecosystem/apps/");
  const data = await page.evaluate(() => document.querySelector('*').outerHTML);
  await browser.close();
  const t = data.split('<span data-v-55771fb7=""')
  let listProjects = []
  for (let i = 0; i < t.length; i++) {
    let t1 = t[i].split('rel="noreferrer noopener">')
    if(t1.length > 1)
    listProjects.push(t1[t1.length - 1])
  }
  console.log("Current project: " + listProjects.length)

let lines = await readLastLines.read('listCosmosProjects.txt', 1)
//console.log("lines: " + lines.length)
let oldProject = []
if(lines.length > 0)
    oldProject = lines.split(', ')
console.log("oldProject: " + oldProject.length)

newProject = listProjects.filter( function( el ) {
    return lines.indexOf( el ) < 0;
  });
console.log("newProject: " + newProject)
if (newProject.length > 0)
    fs.appendFile('listCosmosProjects.txt', '\n' + listProjects.join(', '), function (err) {
        if (err) throw err;
    });
})();
