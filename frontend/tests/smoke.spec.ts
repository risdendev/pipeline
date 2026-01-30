import { test, expect} from '@playwright/test';

test('app loads @smoke', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByRole('heading', { name: 'Analytics Platform'})).toBeVisible();
})
