---
title: "Equipments"
permalink: /equipments/
excerpt: "Hardware used in the RASSP lab."
author_profile: true
---

{% comment %} Content comes from _data/equipment.yml {% endcomment %}
{% include placeholder-mode %}

{% assign items = site.data.equipment %}
{% unless show_placeholders %}{% assign items = items | where_exp: "e", "e.placeholder != true" %}{% endunless %}

{% if items.size > 0 %}
<ul class="item-list">
{% for item in items %}
  <li class="item-card">
    {% if item.image %}
    <div class="item-card__image">
      <img src="{{ item.image | prepend: '/images/' | relative_url }}" alt="{{ item.image_alt }}" loading="lazy">
    </div>
    {% endif %}
    <div class="item-card__body">
      {% if item.type %}<p class="item-card__meta">{{ item.type }}</p>{% endif %}
      <h2 class="item-card__title">{{ item.name }}</h2>
      {{ item.description | markdownify }}
    </div>
  </li>
{% endfor %}
</ul>
{% else %}
<p>The list of lab equipment will be available soon.</p>
{% endif %}
