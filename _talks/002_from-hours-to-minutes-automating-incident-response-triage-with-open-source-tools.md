---
accepted: true
code: JUQMKN
details: true
keynote: false
layout: talk
room: Westin - Partenkirchen
speakers:
- bio: "Markus Einarsson is a Security Architect and Incident Response Lead at Sectra
    in Sweden, where he secures cloud-hosted environments for healthcare customers
    worldwide. With over a decade of experience in cybersecurity, Markus specializes
    in incident response, digital forensics and security architecture.\r\n\r\nAs part
    of the Sectra Hunt and Incident Response Team, he has extensive hands-on experience
    with forensic workflows and modern DFIR toolchains. Markus holds multiple GIAC
    certifications including GEIR, GCDA, GCFE, GCFA, GRID, GNFA, GCIA and GCIH. He
    is passionate about scalable incident response methodologies and advancing open-source
    forensic tools."
  handle: false
  name: Markus Einarsson
  photo: img/speakers/XXEWP9.webp
timeslot:
  duration: 30
  end: 2025-11-17 10:30:00+01:00
  start: 2025-11-17 10:00:00+01:00
title: 'From Hours to Minutes: Automating Incident Response Triage with Open-Source
  Tools'
track: 2
---

Traditional forensic acquisitions create bottlenecks in incident response, requiring specialized expertise and significant time that delays investigations.
This presentation introduces an automated forensic triage workflow using open-source tools to accelerate response operations.

The workflow utilizes a Velociraptor offline collector to acquire forensic triage images, automatically uploaded to cloud storage.
This triggers an OpenRelik workflow that processes triage data using tools like Hayabusa and Plaso/log2timeline, with AI-powered analysis and summarization.
The processed output is uploaded to Timesketch for collaborative analysis.

Several DFIR datasets will be used to show the automation pipeline from initial collection to timeline analysis.
The workflow reduces time-to-analysis from hours to minutes while maintaining forensic integrity.

Attendees will learn to implement automated triage workflows and integrate multiple open-source tools into investigation pipelines.
This targets incident responders, digital forensics practitioners and anyone in the security community looking to streamline forensic operations.