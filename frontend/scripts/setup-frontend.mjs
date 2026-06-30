import { writeFileSync } from 'fs';

const html = [
  '<!doctype html>',
  '<meta charset="UTF-8">',
  '<title>DAEDALUS</title>',
  '<div id="root"></div>',
  '<' + 'script type="module" src="/src/main.tsx"></' + 'script>',
  '',
].join('\n');

const vite = [
  "import { defineConfig } from 'vite';",
  "import react from '@vitejs/plugin-react';",
  '',
  "export default defineConfig({plugins: [react()], server: {host: '0.0.0.0', port: 5173}});",
  '',
].join('\n');

writeFileSync('index.html', html);
writeFileSync('vite.config.ts', vite);
console.log('DAEDALUS frontend setup complete.');
