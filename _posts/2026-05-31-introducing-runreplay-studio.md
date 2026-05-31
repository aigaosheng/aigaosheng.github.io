---
layout: post
title: "RunReplay Studio- Turn Your Apple Health Runs into Narrated Tour-Guide Videos"
date: 2026-05-31 23:10:28 +0800
type: post
published: true
status: publish
categories: []
tags:
- web-app
- gpx
- apple-health
- webcodecs
- openstreetmap
keywords: [web-app, gpx, apple-health, webcodecs, openstreetmap]
permalink: /RunReplay Studio- Turn Your Apple Health Runs into Narrated Tour-Guide Videos/
---

## RunReplay Studio: Turn Your Apple Health Runs into Narrated Tour-Guide Videos

You finished a run along the river, or wandered a new city on foot, and your
watch quietly recorded every step. That GPX track is a story — but it usually
dies in an app as a thin line on a map.

**RunReplay Studio** turns that line into a story worth watching.

Drop in a GPX file (or your whole Apple Health export), and the app builds a
**publish-ready replay video**: an animated avatar runs your exact route over a
live map, and as it passes real landmarks, a neural voice narrates their
history — like a tour guide walking the route beside you. The finished clip
exports as a frame-accurate **MP4**, entirely in your browser.


---

## It's a tour guide, not just a route animation

This was the whole idea. Plenty of tools can draw a dot moving along a track.
RunReplay goes further: it figures out **which famous places you actually passed**
and tells you about them.

Here's how it works under the hood:

1. **Parse your route.** GPX from Apple Fitness, Strava, Garmin — anything
   standard. Missing timestamps or elevation? It fills in sensibly.
2. **Find the landmarks.** It queries [OpenStreetMap](https://www.openstreetmap.org)
   for notable places near your path — museums, monuments, temples, towers,
   parks — preferring the famous, Wikipedia-tagged ones.
3. **Tell their story.** For each landmark it pulls a real description **and a
   photo** straight from Wikipedia, then writes a tour-guide narration line:
   _"Coming up, Tan Si Chong Su. Ancestral Hall of the Tan Clan, a Chinese
   temple built between 1876 and 1878…"_
4. **Bring it to life.** The narration is spoken by a neural voice, the landmark
   photo slides onto the screen, and the avatar talks as it passes.

If a stretch of your route is quiet and passes nothing famous, it degrades
gracefully — you still get clean checkpoints, just without the stories.

## What's in the box

- 🗺️ **Live map replay** — your avatar runs the route on a clean, colorful
  basemap, with landmark pins you can tap for a photo and a story.
- 🎙️ **Real narration** — historical blurbs and photos sourced live from
  Wikipedia & Wikimedia, spoken by a neural voice. **Pick your guide's voice**
  (US / UK, male / female).
- 🎬 **Cinematic intro** — the route draws itself on, a title card appears, then
  a smooth follow-cam takes over for the run.
- 🏷️ **Smart titles** — the app reverse-geocodes your route into a friendly name
  like _"Tiong Bahru Run"_ (and you can rename it before exporting).
- 🍎 **Apple Health friendly** — upload your `export.zip` directly; if it
  contains many workout routes, just pick the one you want.
- 🎵 **Make it yours** — choose an avatar, drop in a music bed, or replace the
  map with your own background image.
- 📲 **Export anywhere** — Shorts/Reels (9:16) or YouTube (16:9), 8–30 seconds,
  as a frame-accurate **H.264 + AAC MP4**.

## Your data never leaves your machine

This is the part I'm proudest of. RunReplay Studio is **100% client-side**:

- **No server.** Everything — parsing, rendering, voice synthesis, video
  encoding — runs in your browser tab.
- **No API keys, no accounts.** It uses only free, open services: OpenStreetMap
  Overpass for landmarks, Wikipedia/Wikimedia for stories and photos, and
  Nominatim for place names.
- **No uploads.** Your GPS track isn't sent to anyone. Your run stays yours.

The MP4 is encoded right on the page using the browser's
[WebCodecs API](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API) —
the same low-level video tech that powers modern web video — so exports are
frame-accurate instead of screen-recorded.

## A few honest notes

- **Use a Chromium browser (Chrome/Edge) for MP4 export.** WebCodecs isn't
  everywhere yet; other browsers fall back to WebM.
- **First export downloads the neural voice model** (~once, cached after). If it
  can't load, the video still exports with on-screen captions.
- **Landmark richness depends on your route.** A run past a heritage district
  lights up with stories; a quiet suburban loop will have fewer.

## Under the hood (for the curious)

It's a no-bundler, no-build app — just ES modules and a handful of CDN
libraries. The logic core (GPX parsing, distance math, landmark placement,
narration text) is **pure and unit-tested**; the browser-only bits (Leaflet
map, neural TTS, canvas compositing, WebCodecs muxing) sit on top. Motion is
**distance-based**, so the avatar moves evenly even when GPS samples are
uneven, and every frame is rendered then encoded one-by-one for a deterministic
result.

---

## Take your next run for a spin

Your runs already tell a story. RunReplay Studio just gives them a voice.

Load the demo loop to see it in action, then drop in your own GPX and watch your
route become a narrated tour.
