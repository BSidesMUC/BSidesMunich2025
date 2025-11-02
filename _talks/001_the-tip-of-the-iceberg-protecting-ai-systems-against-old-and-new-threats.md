---
accepted: true
code: FQXFL3
details: true
keynote: false
layout: talk
room: Westin - Munich
speakers:
- bio: I am a senior security consultant, founder and a director at the Munich based
    company secureIO GmbH. With a strong background in application security and building
    and managing application security programs, I am passionate about all things related
    to AppSec and DevSecOps.
  handle: false
  name: Michael Helwig
  photo: img/speakers/VTB8G9.webp
- bio: "Benjamin began his career as a Cyber Security Consultant and has since developed
    into a specialist at the intersection of machine learning and security. His work
    focuses on the practical evaluation and implementation of the **OWASP Top 10**
    for **Machine Learning** and **Large Language Models (LLMs)**, particularly through
    hands-on experience with **RAG**-based LLM systems in real-world security contexts.
    \r\n\r\nBenjamin also works on secure system design, applying threat modeling
    and Security by Design in alignment with ISMS principles. His current research
    includes supervised learning techniques to reduce false positives in vulnerability
    detection, as well as risk analysis in LLM systems – always aiming to bridge the
    gap between research and secure implementation."
  handle: false
  name: Benjamin Altmiks
  photo: img/speakers/8HQCQV.webp
timeslot:
  duration: 30
  end: 2025-11-17 16:30:00+01:00
  start: 2025-11-17 16:00:00+01:00
title: 'The Tip of the Iceberg: Protecting AI Systems Against Old and New Threats'
track: 1
---

AI applications surface new, visible risks—but underneath lie amplified traditional ones.
The massive data aggregation, probabilistic outputs, and decision‑making power of AI systems make them inherently more critical.
To defend these systems, we must extend our security programs and rediscover the strength of foundational security principles.
In this talk, we will examine new threats to AI applications, distinguish them from familiar "old" threats, and explore both through a practical threat model of a real‑world AI deployment.

We are using the iceberg metaphor to visualize the relationship between old and new risks.
This image operates on multiple levels.
Above the surface you see prompt injection, hallucinations… but beneath the waves lie familiar threats and traditional risks—amplified data exposure, access control failures, insecure components.
The thesis is simple: new AI risks are real—but don’t throw out your classic AppSec toolkit.

In another interpretation, the image also illustrates how AI applications often function: only a thin layer—usually the API interface—is exposed.
Beneath the surface, however, lies a vast repository of data and capabilities (agents) that pose the real danger if compromised.
It’s also crucial to consider how AI is integrated into the business case, as that integration directly influences the system’s criticality.

In the example of a real‑world AI application—a RAG‑based scenario—we’ll explore how to conduct risk assessment and threat modeling for AI systems, and examine the role of traditional security measures.
We show how classic defenses remain vital for protecting AI applications as we walk through a hands‑on threat‑modeling case.
We cover the threat‑modeling process, highlight the new dimensions introduced by AI (including how to seamlessly incorporate EU AI Act requirements), and demonstrate how to include AI‑specific risks into your existing threat‑modeling workflows.