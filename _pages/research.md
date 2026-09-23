---
title: "Research"
permalink: /research/
excerpt: "Research themes of the RASSP group."
author_profile: true
---

{% comment %} Content comes from _data/research.yml {% endcomment %}

<ul class="item-list">
{% for theme in site.data.research %}
  <li class="item-card" id="{{ theme.id }}">
    {% if theme.image %}
    <div class="item-card__image">
      <img src="{{ theme.image | prepend: '/images/' | relative_url }}" alt="{{ theme.image_alt }}" loading="lazy">
    </div>
    {% endif %}
    <div class="item-card__body">
      <h2 class="item-card__title">{{ theme.title }}</h2>
      {{ theme.summary | markdownify }}
      {% if theme.related_publications and theme.related_publications.size > 0 %}
      <p><strong>Related publications:</strong></p>
      <ul>
        {% for slug in theme.related_publications %}
          {% assign pub_path = "_publications/" | append: slug | append: ".md" %}
          {% assign pub = site.publications | where: "relative_path", pub_path | first %}
          {% if pub %}<li><a href="{{ pub.url | relative_url }}">{{ pub.title }}</a> ({{ pub.date | date: "%Y" }})</li>{% endif %}
        {% endfor %}
      </ul>
      {% endif %}
    </div>
  </li>
{% endfor %}
</ul>
