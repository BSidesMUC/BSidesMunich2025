---
accepted: true
code: CSSYPY
details: true
keynote: false
layout: talk
room: Westin - Munich
speakers:
- bio: Hi, I'm Oisín, a cloud security engineer at Immersive, a company specialising
    in practical cybersecurity training. I've spent the past five years there honing
    my cloud security skills, with experience across all the major public cloud providers.
    I love learning about and evaluating cutting-edge research from across the cloud
    security field, so I can teach others all about the latest trends, tactics, and
    techniques. I'm especially enthusiastic about AWS and promoting secure practices
    in cloud infrastructure.
  handle: false
  name: Oisin B
  photo: img/speakers/JEQUDB.png
timeslot:
  duration: 30
  end: 2025-11-17 15:00:00+01:00
  start: 2025-11-17 14:30:00+01:00
title: 'The Perks and Perils of Persistence: AWS Attacker Techniques'
track: 1
---

Once an attacker has gained initial access to an AWS account, one of their first steps is to build persistence.
Their retained access can last even after defenders have already begun to isolate and contain an attack.
This talk will evaluate the advantages and drawbacks of attacker persistence techniques in AWS, comparing their complexity, potential for compromise, and how easy they are to detect.

Of course, an attacker's choice of persistence methods can depend heavily on the permissions available to them and the target they’re after, and there are a myriad of different ways to build persistence.
Therefore, the aim here isn’t to cover every possible persistence method in AWS.
Instead, this talk will cover some of the more common methods that have been seen in the wild, and draw your attention to some of the more niche techniques that are still worth looking out for and locking down.

Finally, for each technique, this talk will review practical detection and prevention methods and the considerations of these.