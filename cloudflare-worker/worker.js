/**
 * Cloudflare Worker — LeetCode GraphQL Proxy  (v2 — fixed query)
 * =====================================================================
 * Deployed at: https://leetcode-heatmap.adarsharya7073.workers.dev/
 *
 * WHY this worker exists:
 *   LeetCode's GraphQL API blocks cross-origin requests from browsers.
 *   This Worker forwards the request server-side and injects CORS headers.
 *
 * FIX (v2):
 *   The old query used `userProgressCalendarV2` which LeetCode now blocks
 *   for unauthenticated requests.  This version uses `matchedUser.userCalendar`
 *   which is still publicly accessible without authentication.
 *
 * HOW TO DEPLOY:
 *   Option A — Cloudflare Dashboard (easiest):
 *     1. Go to workers.cloudflare.com → your worker → "Edit Code"
 *     2. Paste this entire file and click "Save & Deploy"
 *
 *   Option B — Wrangler CLI:
 *     npx wrangler deploy
 * =====================================================================
 */

const LEETCODE_GQL = 'https://leetcode.com/graphql';

// Headers sent to LeetCode — mimic a real browser to avoid bot detection
const LC_HEADERS = {
  'Content-Type':    'application/json',
  'Referer':         'https://leetcode.com/',
  'Origin':          'https://leetcode.com',
  'User-Agent':      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'Accept':          'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control':   'no-cache',
  'x-csrftoken':     ''   // empty is fine for public/unauthenticated queries
};

// CORS headers returned to the browser
const CORS_HEADERS = {
  'Access-Control-Allow-Origin':  '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Content-Type':                 'application/json'
};

export default {
  async fetch(request, env, ctx) {

    /* ── Handle CORS pre-flight (OPTIONS) ── */
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    /* ── Reject non-POST requests ── */
    if (request.method !== 'POST') {
      return new Response(
        JSON.stringify({ error: 'Only POST requests are accepted' }),
        { status: 405, headers: CORS_HEADERS }
      );
    }

    /* ── Parse incoming body ── */
    let body;
    try {
      body = await request.json();
    } catch {
      return new Response(
        JSON.stringify({ error: 'Invalid JSON body' }),
        { status: 400, headers: CORS_HEADERS }
      );
    }

    /* ── Forward to LeetCode GraphQL ── */
    let lcResponse;
    try {
      lcResponse = await fetch(LEETCODE_GQL, {
        method:  'POST',
        headers: LC_HEADERS,
        body:    JSON.stringify(body)
      });
    } catch (err) {
      return new Response(
        JSON.stringify({ error: 'Failed to reach LeetCode', detail: err.message }),
        { status: 502, headers: CORS_HEADERS }
      );
    }

    /* ── Return LeetCode's response with CORS headers ── */
    const data = await lcResponse.text();
    return new Response(data, {
      status:  lcResponse.status,
      headers: CORS_HEADERS
    });
  }
};
