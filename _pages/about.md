---
permalink: /
title: "RAdar and Sonar Signal Processing Research Group"
excerpt: "RASSP develops signal processing and machine learning methods for radar and sonar sensing."
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<img class="home-logo" src="{{ '/images/rassp_logo.svg' | relative_url }}" alt="RASSP logo: a radar and sonar emblem next to the words RASSP, Radar and Sonar Signal Processing Research Group" width="920" height="260">

<!-- TODO: review the mission statement below and replace it with the group's own wording. -->
RASSP is a research group in the [Department of Electronics and Communication Engineering](https://ehb.itu.edu.tr/en) at [Istanbul Technical University](https://www.itu.edu.tr), working on signal processing for radar and sonar systems. We develop methods that see beneath the ground surface and below the waterline, from classical and tensor-based techniques to modern deep learning, and we bring them to real-time embedded platforms.

Research interests
------

{% for theme in site.data.research -%}
- [{{ theme.title }}]({{ '/research/' | relative_url }}#{{ theme.id }})
{% endfor %}

{% include placeholder-mode %}
{% assign news = site.data.news | sort: "date" | reverse %}
{% unless show_placeholders %}{% assign news = news | where_exp: "n", "n.placeholder != true" %}{% endunless %}
{% if site.news_on_home > 0 and news.size > 0 %}
Latest news
------

<ul class="news-list">
{% for item in news limit: site.news_on_home %}
  <li><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%b %-d, %Y" }}</time><div>{{ item.text | markdownify | remove: '<p>' | remove: '</p>' }}</div></li>
{% endfor %}
</ul>

[All news]({{ '/news/' | relative_url }})
{% endif %}

<div class="wave-divider" role="presentation"></div>

See our [research]({{ '/research/' | relative_url }}), [publications]({{ '/publications/' | relative_url }}) and [people]({{ '/people/' | relative_url }}), or [get in touch]({{ '/contact/' | relative_url }}).
