---
title: "People"
permalink: /people/
excerpt: "Members of the RASSP group."
author_profile: true
---

{% comment %} Content comes from _data/people.yml {% endcomment %}
{% include placeholder-mode %}

{% assign roles = "pi,faculty,phd,msc,undergrad,alumni" | split: "," %}
{% assign headings = "Group Leader,Researchers,PhD Students,MSc Students,Undergraduate Students,Alumni" | split: "," %}

{% for role in roles %}
  {% assign members = site.data.people | where: "role", role %}
  {% unless show_placeholders %}{% assign members = members | where_exp: "m", "m.placeholder != true" %}{% endunless %}
  {% if members.size > 0 %}
<h2 id="{{ role }}">{{ headings[forloop.index0] }}</h2>
<ul class="people-grid">
  {% for person in members %}{% include person-card.html person=person %}{% endfor %}
</ul>
  {% endif %}
{% endfor %}
