# Cloudflare Worker Deployment (v2 Fix)

The `worker.js` has been updated to fix the LeetCode heatmap.

## What changed
- **Old query** (`userProgressCalendarV2`) → now **blocked** by LeetCode for unauthenticated requests
- **New query** (`matchedUser.userCalendar`) → still publicly accessible

## Redeploy via Dashboard (Easiest)

1. Go to [workers.cloudflare.com](https://workers.cloudflare.com)
2. Open your worker: **leetcode-heatmap**
3. Click **Edit Code**
4. Replace ALL content with the contents of `worker.js` (in this folder)
5. Click **Save & Deploy**

## Redeploy via Wrangler CLI

```bash
cd cloudflare-worker
npx wrangler deploy
```
