# Digital Health Awareness Campaign

**"Digital Knowledge for a Healthier Nepal"**

A CMS-driven Django + PostgreSQL platform for a Nepal-focused digital health
literacy campaign. Public pages are server-rendered from Django templates;
a DRF API exposes the same content for a future mobile app.

All 18 phases from the original spec are implemented. See "What's built"
below for the honest state of each piece.

## Stack

- Django 5 + Django REST Framework
- PostgreSQL
- HTML5 / CSS3 / vanilla JS (no frontend framework)
- WhiteNoise for static files, django-storages ready for S3/Cloudinary/R2

## Local setup

1. **Clone and create a virtualenv**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL** (locally or via Docker)
   ```bash
   createdb digital_health_campaign
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env`:
   - `SECRET_KEY` — generate one, e.g. `python -c "import secrets; print(secrets.token_urlsafe(50))"`
   - `DB_NAME`, `DB_USER`, `DB_PASSWORD` — match your local Postgres role/db
   - Leave `USE_S3=False` for local development (media saves to `/media`)

4. **Run migrations and create an admin user**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Run the dev server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` for the site and `/admin/` for Django Admin.
   On first run, log into `/admin/` and fill in **Campaign Settings** (name,
   slogan, hero text, stats, contact/socials) — every template reads from
   that one row instead of hard-coded values.

## Project structure

```
config/            Django settings, root urls, wsgi/asgi
apps/               One Django app per CMS-managed section
  core/             CampaignSettings singleton, homepage, shared context processor
  campaigns/        Campaign Areas (districts) — Phase 6
  health/           Digital Health Tools + Preventive Health topics — Phase 7
  resources/        Resource library — Phase 8
  activities/       Activities — Phase 9
  news/             News & Updates — Phase 9
  team/             Team members — Phase 10
  gallery/          Photo/video gallery — Phase 10
  volunteers/       Volunteer applications — Phase 11
  contact/          Contact form — Phase 11
templates/          base.html + includes/ + one folder per app
static/             css/, js/, images/
media/              User-uploaded files (local dev only; see USE_S3)
```

Each `apps/<name>` has real models, admin, views, URLs, and (for the 8
public-facing apps) DRF serializers + API endpoints. `core` additionally
holds the CampaignSettings singleton, homepage/about/mission/objectives
views, sitemap, robots.txt, and global search.

## What's built

| Phase | Status | Notes |
|---|---|---|
| 1. Project setup | Done | Modular `apps/` layout, `.env`-driven settings |
| 2. Design system | Done | `static/css/style.css` — teal/blue/green palette, Inter + Noto Sans Devanagari |
| 3. Navbar + footer | Done | Sticky nav, mobile hamburger, language switcher (UI only — see note below), full footer |
| 4. Homepage | Done | All 15 sections in spec order, pulling live data from every app |
| 5. About/Mission/Objectives | Done | `apps/core` — Objectives page content is placeholder text, clearly labeled "Sample Data" |
| 6. Campaign Areas + map | Done | `apps/campaigns` — honest positional grid (admin sets `map_x`/`map_y` per district), not a fake Nepal outline; swap in a real SVG later using the same coordinates |
| 7. Digital Health / Preventive Health | Done | `apps/health` — two models, category filters |
| 8. Resources | Done | `apps/resources` — search, category + type filters, pagination |
| 9. Activities + News | Done | `apps/activities`, `apps/news` — list/detail, related posts |
| 10. Team + Gallery | Done | `apps/team`, `apps/gallery` — masonry grid, lightbox |
| 11. Volunteer + Contact forms | Done | `apps/volunteers`, `apps/contact` — Django forms, success messages, CSV export for volunteer applications in Admin |
| 12. Models | Done | Across all 9 content apps, real migrations generated and tested |
| 13. Django Admin | Done | Every model registered with search/filter/list-editable |
| 14. DRF API | Done | Read-only endpoints for every public app, matching the spec's URL list exactly |
| 15. Frontend ↔ dynamic data | Done | All templates render from the database; global search (`/search/`) queries live models |
| 16. Auth/security | Done | CSRF, secure cookies in production, env-only secrets, no PII exposed via public views or API |
| 17. Performance/accessibility/SEO | Done | Lazy-loaded images, skip link, focus states, semantic headings, `sitemap.xml`, `robots.txt`, meta/OG tags |
| 18. Deployment prep | Done | `Procfile`, `runtime.txt`, WhiteNoise static serving, S3-ready media storage |

**Tested end-to-end**: every page and API endpoint returns 200 with seeded
sample data, both form submissions (volunteer + contact) save correctly and
redirect properly, and Django Admin is fully functional for every model.

**Two things worth knowing before you treat this as finished:**
- **Language switcher is UI-only.** The `EN | नेपाली` links in the navbar
  don't yet swap content — per spec section 29, this needs a real bilingual
  content architecture (e.g. parallel fields on each model, or
  `django-modeltranslation`), which is a content-modeling decision worth
  making deliberately rather than bolting on.
- **Objectives page text and the districts-overview pin positions are
  placeholder/sample data** — replace with verified content in Django Admin.

## Deployment

1. Set `DEBUG=False` and a real `ALLOWED_HOSTS` in your production `.env`.
2. Provision a managed PostgreSQL instance and point `DB_*` vars at it.
3. Set `USE_S3=True` and fill in the `AWS_*` vars once you have a bucket
   (S3, R2, or any S3-compatible provider) — media then serves from there
   instead of local disk.
4. `python manage.py collectstatic` (WhiteNoise serves the result).
5. Deploy with the included `Procfile`:
   - `release: python manage.py migrate --noinput` runs on each deploy
   - `web: gunicorn config.wsgi:application` serves the app
6. Point your CDN/DNS at the app host; static files are compressed and
   hashed by WhiteNoise automatically.

## Build order (for reference / re-runs)

Matches the phased plan in the original spec — each phase was built and
smoke-tested as a separate step rather than all at once:

1. Project setup · 2. Design system · 3. Navbar + footer · 4. Homepage ·
5. About/Mission/Objectives · 6. Campaign Areas + map · 7. Digital Health +
Preventive Health · 8. Resources · 9. Activities + News · 10. Team + Gallery ·
11. Join Campaign + Contact · 12. Models · 13. Admin · 14. DRF API ·
15. Connect frontend to dynamic data · 16. Auth/security · 17. Performance/
accessibility/SEO · 18. Deployment prep

## Notes

- No secrets are hard-coded — everything sensitive comes from `.env`
  (see `.env.example`).
- `USE_S3` in `.env` toggles between local media storage and S3/R2/
  Cloudinary; the setting is already wired in `config/settings.py`.
- Sample/placeholder content added in later phases should be clearly
  labeled "Sample Data" and never presented as verified campaign statistics.
