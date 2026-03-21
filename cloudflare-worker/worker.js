/**
 * Cloudflare Worker — LeetCode GraphQL Proxy
 * =====================================================================
 * Deployed at: https://leetcode-heatmap.adarsharya7073.workers.dev/
 *
 * WHY this worker exists:
 *   LeetCode's GraphQL API (https://leetcode.com/graphql) blocks cross-origin
 *   requests from browsers (CORS policy).  Server-to-server requests are NOT
 *   subject to CORS, so this Worker forwards the request on behalf of the
 *   browser and injects the required CORS response headers.
 *
 * WHAT was wrong with the old worker (root cause):
 *   Most likely one or more of these:
 *     1. Missing  Access-Control-Allow-Origin  header → browser blocked result
 *     2. Missing  OPTIONS pre-flight handler   → POST never sent
 *     3. LeetCode started requiring  Referer  or  User-Agent  headers (bot block)
 *     4. Worker CPU time exceeded on free tier (complex query)
 *     5. Worker not actually deployed / route not matched
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

// Headers sent to LeetCode — mimic a real browser to avoid bot blocks
const LC_HEADERS = {
  'Content-Type':  'application/json',
  'Referer':       'https://leetcode.com/',
  'Origin':        'https://leetcode.com',
  'User-Agent':    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'Accept':        'application/json',
  'x-csrftoken':   ''   // empty is fine for public queries
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

    /* ── Forward request to LeetCode GraphQL ── */
    let body;
    try {
      body = await request.json();
    } catch {
      return new Response(
        JSON.stringify({ error: 'Invalid JSON body' }),
        { status: 400, headers: CORS_HEADERS }
      );
    }

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

    /* ── Return LeetCode's response with CORS headers attached ── */
    const data = await lcResponse.text();
    return new Response(data, {
      status:  lcResponse.status,
      headers: CORS_HEADERS
    });
  }
};
