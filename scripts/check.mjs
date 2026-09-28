import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve(process.cwd());
const htmlFiles = fs.readdirSync(root).filter(f => f.endsWith('.html'));
const required = ['index.html','about.html','practice-areas.html','advocate.html','insights.html','contact.html','privacy.html','terms.html','404.html'];
const errors=[];
for (const f of required) if (!htmlFiles.includes(f)) errors.push(`Missing ${f}`);
for (const file of htmlFiles) {
  const txt=fs.readFileSync(path.join(root,file),'utf8');
  if (!txt.includes('<meta name="viewport"')) errors.push(`${file}: viewport missing`);
  if (!txt.includes('assets/css/site.css')) errors.push(`${file}: stylesheet missing`);
  const re=/(?:src|href)="(\/assets\/[^"?#]+)"/g;
  for (const m of txt.matchAll(re)) {
    const target=path.join(root,m[1].slice(1));
    if (!fs.existsSync(target)) errors.push(`${file}: broken local asset ${m[1]}`);
  }
}
const css=fs.readFileSync(path.join(root,'assets/css/site.css'),'utf8');
if (!css.includes('@media (max-width:620px)')) errors.push('mobile breakpoint missing');
if (!fs.existsSync(path.join(root,'assets/video/logo-animation-4k60.mp4'))) errors.push('logo animation missing');
if (errors.length) { console.error('\nCHECK FAILED\n- '+errors.join('\n- ')); process.exit(1); }
console.log(`CHECK PASSED: ${htmlFiles.length} HTML pages, local assets verified, mobile CSS present.`);
