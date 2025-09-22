---
accepted: true
code: 9ELMEK
details: true
keynote: false
layout: talk
room: Westin - Partenkirchen
speakers:
- bio: Guillaume is a penetration tester and security researcher working at Synacktiv.
    During his career, he developed a healthy addiction to Windows systems and their
    internals. He is also passionate about Active Directory security, in which he
    gathered solid knowledge through several Red Team engagements and internal pentests.
  handle: false
  name: Guillaume André
  photo: false
- bio: Wilfried Bécard is a hacker and researcher working at Synacktiv. With a particular
    interest in Active Directory and Azure exploitation, his passion lies in uncovering
    new techniques to enhance cybersecurity in these areas. Constantly experimenting,
    testing, and collaborating with the security community, he aims at constantly
    improving his knowledge in these fields.
  handle: false
  name: Wil
  photo: img/speakers/RSK9M3.jpg
timeslot:
  duration: 30
  end: 2025-11-17 16:30:00+01:00
  start: 2025-11-17 16:00:00+01:00
title: 'NTLM reflection is dead, long live NTLM reflection: Story of an accidental
  Windows RCE'
track: 2
---

For nearly two decades, Windows has been plagued with NTLM reflection vulnerabilities.
This special case of NTLM authentication relay has historically led to local privilege escalation or even remote command execution, although with some limitations.
Over time, mitigations against this class of vulnerability were implemented, leading to a false assumption that NTLM reflection attacks were relics of the past.
This presentation will shatter that assumption by covering the research that led to the discovery of CVE-2025-33073, a logical vulnerability leading to authenticated RCE as SYSTEM on almost any Windows machine and without any user interaction.

In this talk, fundamental concepts about authentication relay attacks will be explained, as well as the context surrounding the research and the accidental discovery of the vulnerability.
Afterwards, a methodical investigation of the root cause of the vulnerability will be presented, first by analysing network captures and then by performing a thorough reverse-engineering of LSASS internals and its NTLM authentication provider.


Subsequently, we will shift our attention to Kerberos, where we will demonstrate that CVE-2025-33073 is not restricted to NTLM and that it also affects Kerberos.
After a brief reminder of the protocol, in-depth insights in its integration within LSASS will be discussed as well as an undocumented behavior, to understand why this vulnerability also applies to Kerberos.

Finally, the patch analysis will be presented.
We will detail how it fixes the specific attack vector described in this presentation and how it may not be enough to completely eradicate this class of vulnerability.
We will conclude by explaining how the exploitation of this vulnerability could have been prevented even before it was found and the current state Windows machine hardening.