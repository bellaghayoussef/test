const puppeteer = require('puppeteer');
const express = require('express');
const app = express();

app.get('/api/boutiques', async (req, res) => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://vitrina.hstn.me/api/boutiques');
  const content = await page.evaluate(() => {
    return JSON.parse(document.body.innerText); // extract JSON
  });
  await browser.close();
  res.json(content);
});

app.listen(3000, () => console.log('Proxy running on port 3000'));