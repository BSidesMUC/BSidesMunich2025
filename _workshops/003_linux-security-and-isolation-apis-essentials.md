---
accepted: true
code: YPQGKD
details: true
keynote: false
layout: workshop
room: Hochschule München - R1.008
speakers:
- bio: Michael Kerrisk is a trainer, author, and programmer who has a passion for
    investigating and explaining software systems. He is the author of "The Linux
    Programming Interface", a widely acclaimed book on Linux (and UNIX) system programming.
    He has been actively involved in the Linux development community since 2000, operating
    mainly in the area of testing, design review, and documentation of kernel-user-space
    interfaces. From 2004 to 2021, he maintained the Linux "man-pages" project, which
    provides the primary documentation for Linux system calls and C library functions.
    Michael is a New Zealander, living in Munich, Germany, from where he operates
    a training business (man7.org) providing low-level Linux programming courses in
    Europe, North America, and occasionally further afield.
  handle: false
  name: Michael Kerrisk
  photo: img/speakers/XRZ3WN.jpg
timeslot:
  duration: 480
  end: 2025-11-15 17:00:00+01:00
  start: 2025-11-15 09:00:00+01:00
title: Linux Security and Isolation APIs essentials
track: 3
---

This full-day workshop provides an overview of the low-level Linux features–capabilities, namespaces, and control groups (cgroups)–that are used to build containers and sandboxes. Beginning with classical privileged programs (set-UID-root programs), we look at how capabilities and namespaces can be used to place processes in “a world of their own” in which they have private instances of various “global” resources. Those features–user namespaces in particular–can also be used to implement the notion of a process that is superuser inside a container while being unprivileged outside the container. Finally, we’ll see how cgroups can be used to limit resource consumption, so that the processes in a container can’t negatively impact other users on the system. You can find some further detail on the workshop content at https://man7.org/training/sisess/sisess_course_outline.html and https://man7.org/training/sisess/.