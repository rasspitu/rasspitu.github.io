---
title: "Contact"
permalink: /contact/
excerpt: "How to reach the RASSP group."
author_profile: true
---

<!-- TODO: add the faculty / department, building and room, full postal address and group email. -->

**RASSP Research Group**<br>
Istanbul Technical University<br>
Istanbul, Türkiye

{% if site.author.email %}
Email: [{{ site.author.email }}](mailto:{{ site.author.email }})
{% endif %}

{% for p in site.data.people %}{% if p.role == "pi" or p.role == "faculty" %}{% if p.email %}
- **{{ p.name }}** ({{ p.title }}): [{{ p.email }}](mailto:{{ p.email }})
{% endif %}{% endif %}{% endfor %}

For questions about a specific project, you can also contact the [group members]({{ '/people/' | relative_url }}) directly.

University website: [www.itu.edu.tr](https://www.itu.edu.tr)
