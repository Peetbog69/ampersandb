# & Shared Note

**For Nico, Gravy, and Jessica.** One place. No hunting. Updated live.

---

## Currently (June 18)

- **Gravy:** Stripe account created ✓, live keys wired to & bot ✓. Working on video production toolchain (no editing software yet — needs iMovie). Wants to knock out hackathon tasks tonight.
- **Nico:** Just got synced. Found & bot running on VPS (DeepSeek). Caught up on storyboard, task board, hackathon plan. Wired Stripe keys from Whitey67 desktop to & bot. Discovered desktop has computer_use = can review video takes visually.
- **Jessica:** VPS ready, & bot deployed, Stripe tools installed on Whitey67, deploy-agent.sh built. Knows Hermes↔Stripe connection.
- **Marty:** Creative director bot deployed on VPS. Runs DeepSeek V4 Pro. Grey Poupon server. Handles visual/aesthetic review, demo production, brand consistency.

## & Bot Status

| Thing | Status |
|-------|--------|
| Running | ✅ `hermes-gateway-ampersand.service` on vultr-1 |
| Profile | `/root/.hermes/profiles/ampersand/` |
| SOUL | ✅ Butthead energy, 6,123 bytes |
| Model | ⚠️ DeepSeek V4 Pro (hackathon wants Nemotron) |
| VPS Memory | 309MB free / 954MB total |
| Telegram | @Ampersand45_bot |
| Live site | ampersand.foo → links to bot ✅ |

## Hackathon — June 30 (12 days)

**What the demo needs to show:**
1. ✅ & bot greets user (SOUL deployed)
2. ❌ Bot interviews user — onboarding script not built
3. ✅ Takes payment via Stripe ($7/mo) — Keys wired to & bot, gateway restarted
4. ❌ Provisions personal agent — no automation yet
5. ❌ Video production — no editing software, no takes recorded

**NVIDIA angle:** Nemotron 3 Ultra + NemoClaw 2 needs to be VISIBLE in demo. Currently bot runs DeepSeek.

## VPS (vultr-1, 216.128.154.45)

| Service | Profile | Model |
|---------|---------|-------|
| `hermes-gateway-ampersand` | & bot (Butthead) | DeepSeek V4 Pro |
| `hermes-gateway` | Robert (The Cure) | ? |
| `hermes-gateway-marty` | Marty (Creative Director) | DeepSeek V4 Pro |

## Whitey67 (100.102.6.122)

| Service | Profile |
|---------|---------|
| `hermes-gateway` | Jessica (default) |
| `hermes-gateway-jessica` | Jessica (jessica profile) |

## Video Production

- Camera: iPhone
- Screen recording: iPhone (Control Center) + OBS (Mac)
- Editing: **Nothing installed.** Need iMovie (free, App Store).
- Visual review: Nico can use computer_use to see screen and give feedback on takes.
- Storyboard: `docs/DEMO_STORYBOARD.md` (6 scenes, PS2-uncanny aesthetic)

## Immediate Next

1. Install iMovie on MacBook
2. Build onboarding script for & bot
3. Record Scene 1 test take
4. Either switch & bot to Nemotron OR stage Nemotron config shots for demo
5. Get Marty caught up on project context and storyboard

---

*Updated: 2026-06-18 (Nico — Stripe wired, Marty added)*
