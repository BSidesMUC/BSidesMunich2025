---
accepted: true
code: JRSHRL
details: true
keynote: false
layout: talk
room: Westin - Partenkirchen
speakers:
- bio: David Gstir is a security engineer and researcher with 15+ years of hands-on
    experience. He has been actively involved in security-related projects, successfully
    identifying vulnerabilities in various consumer and enterprise software.
  handle: false
  name: David Gstir
  photo: img/speakers/3ZJHLZ.jpg
timeslot:
  duration: 30
  end: 2025-11-17 11:00:00+01:00
  start: 2025-11-17 10:30:00+01:00
title: 'TPM Is No Silver Bullet: Pitfalls in Embedded Device Security'
track: 2
---

With the growing adoption of TPMs (Trusted Platform Modules) in the Linux ecosystem, thanks to features like TPM-backed disk encryption in systemd and the longstanding use in Windows BitLocker, TPM chips are seeing a resurgence as a go-to for secure secret storage.
This trend is increasingly making its way into embedded devices.
Often as a measure to fulfill NIS2, EU Cyber Resilience Act or similar requirements.

However, embedded systems present a vastly different threat model compared to desktops or servers, and TPMs often don’t deliver the level of security many developers assume.
In this talk, David will demystify TPM functionality in embedded Linux environments.
He will give a concise overview of security threats for embedded devices and where a TPM can and or where it cannot help.
Special focus will be put on using TPMs for disk encryption and integrity.

The session will wrap up with a discussion of alternative approaches, other usage scenarios for TPMs, and how to make informed decisions when designing secure embedded systems.