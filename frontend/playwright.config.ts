import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: {
    baseURL: 'http://localhost:5173',
    headless: true,
    browserName: 'chromium',
    launchOptions: {
      slowMo: 1000,
    },
  },
  testDir: './tests',
  testMatch: /.*\.spec\.ts/,
  workers: 1,
  reporter: 'html',
  outputDir: 'test-results',
});
