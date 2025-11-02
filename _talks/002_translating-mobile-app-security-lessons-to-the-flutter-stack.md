---
accepted: true
code: VVSW99
details: true
keynote: false
layout: talk
room: Westin - Partenkirchen
speakers:
- bio: Samuel Hopstock is a software engineer at Guardsquare, where he was one of
    the first engineers working on AppSweep, a mobile app security testing tool. Initially,
    he contributed to the Java bytecode analysis engine for Android apps. Since then
    he has shifted his focus to analyzing and protecting native iOS, Android, and
    Flutter binaries.
  handle: false
  name: Samuel Hopstock
  photo: img/speakers/3DYCUB.webp
timeslot:
  duration: 30
  end: 2025-11-17 12:30:00+01:00
  start: 2025-11-17 12:00:00+01:00
title: Translating mobile app security lessons to the Flutter stack
track: 2
---

Nowadays there’s broad consensus that security is an important topic for app developers.
Unfortunately however, there are still many blog posts, forum discussions, and tutorials out there that propagate some common misconceptions.
Especially apps developed using Flutter, Google's popular cross-platform framework for building native apps from a single Dart codebase:

- “Compiling to native machine code can successfully hide sensitive strings like API keys”
- “There’s a built-in obfuscation mode, so that will protect my sensitive algorithms”
- “There are no reverse engineering tools specifically for Dart yet, so attackers can’t decompile my app”
- “App security scanning tools don’t show findings for my Flutter app, so it must be secure”
- ...

In this talk we put these statements to the test and ask ourselves: “How would an attacker actually approach a Flutter app?”
We start with low-effort wins like finding hardcoded secrets and verbose logging, move to insecure coding practices like weak crypto and broken TLS validation, and finally explore advanced issues like injection attacks and insecure IPC mechanisms.

For each step you’ll see how these issues can be spotted, exploited, and ultimately mitigated - plus practical tips for securing your Flutter apps in development and production.