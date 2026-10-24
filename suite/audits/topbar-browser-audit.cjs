const { chromium } = require('playwright');
const targets = [
  { url: 'https://satoshium.us/suite/', active: 'us' },
  { url: 'https://satoshium.us/suite/interoperability/', active: 'us' },
  { url: 'https://satoshium.ai/', active: 'home' }
];
(async () => {
  const browser = await chromium.launch({headless:true});
  const results = [];
  for (const t of targets) {
    const page = await browser.newPage({viewport:{width:1300,height:800}});
    const requests = [];
    const errors = [];
    page.on('requestfailed', req => { if (/topbar|satoshium\.link\/components/.test(req.url())) requests.push({url:req.url(),failure:req.failure()?.errorText || ''}); });
    page.on('pageerror', e => errors.push(e.message.slice(0,240)));
    let obj = {url:t.url,expected_active:t.active};
    try {
      const response = await page.goto(t.url, {waitUntil:'domcontentloaded',timeout:25000});
      obj.http_status = response?.status() ?? null;
      await page.waitForTimeout(6000);
      obj.topbar_present = await page.locator('#topbar-slot .topbar').count() > 0;
      obj.active_keys = await page.locator('#topbar-slot .topbar .nav a.active').evaluateAll(els=>els.map(e=>e.getAttribute('data-nav')));
      obj.expected_active_found = obj.active_keys.includes(t.active);
      obj.topbar_link_count = await page.locator('#topbar-slot .topbar .nav a').count();
      obj.failed_topbar_requests = requests;
      obj.page_errors = errors;
    } catch(e) {obj.error = String(e).slice(0,350);}
    console.log('BROWSER_AUDIT '+JSON.stringify(obj));
    results.push(obj);
    await page.close();
  }
  await browser.close();
  require('fs').writeFileSync('topbar-browser-results.json',JSON.stringify({results,observedAt:new Date().toISOString()},null,2));
  // Always preserve independent observation; review controls acceptance rather than CI task's status.
})().catch(e=>{console.error(e);process.exit(1)});
