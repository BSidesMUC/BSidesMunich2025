---
accepted: true
code: E9FZQT
details: true
keynote: false
layout: talk
room: Westin - Munich
speakers:
- bio: Stephan Berger has over a decade of experience in cybersecurity. Currently
    working with the Swiss-based company InfoGuard, Stephan investigates breaches
    and hacked networks as Head of Investigation of the Incident Response team. An
    avid Twitter user under the handle @malmoeb, he actively shares insights on cybersecurity
    trends and developments. Stephan also authors the blog DFIR.ch, where he provides
    in-depth analysis and commentary on digital forensics and incident response. Stephan
    has spoken at numerous conferences, sharing his expertise with audiences worldwide.
  handle: false
  name: Stephan Berger
  photo: img/speakers/C7AHN8.webp
timeslot:
  duration: 30
  end: 2025-11-17 10:30:00+01:00
  start: 2025-11-17 10:00:00+01:00
title: Fantastic clear-text passwords and where to collect them
track: 1
---

Dumping LSASS to get passwords, which in the worst case are only hashed… doesn't have to be!

We demonstrate more sophisticated methods for attackers to obtain cleartext passwords.
In the Windows world, we examine Netfilter, Password Filter, and Security Support Providers, which enable custom DLLs to be loaded to capture passwords in cleartext.

Enabling WDigest or searching for passwords in GPO policies are other successful tactics.

Clear-text passwords can also be hidden within command lines or in password properties.

In the Linux world, we have additional techniques to read cleartext passwords.
We provide examples such as backdooring PAM, SSH, or hooking PHP functions.

After taking over VPN appliances, attackers also like to backdoor the login page to send passwords during login to a domain controlled by the attacker.

In our talk, we present not only individual techniques but also real-world examples from various incident response cases, illustrating how these techniques can be detected in logs and through forensic artifacts.

On one hand, experienced red teamers will learn new techniques; on the other hand, blue teamers can benefit from the detection strategies.