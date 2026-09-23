---
title: "News"
permalink: /news/
excerpt: "News from the RASSP group."
author_profile: true
---

{% comment %} Content comes from _data/news.yml {% endcomment %}
{% include placeholder-mode %}

{% assign items = site.data.news | sort: "date" | reverse %}
{% unless show_placeholders %}{% assign items = items | where_exp: "n", "n.placeholder != true" %}{% endunless %}

{% if items.size > 0 %}
<ul class="news-list">
{% for item in items %}
  <li><time datetime="{{ item.date | date: '%Y-%m-%d' }}">{{ item.date | date: "%b %-d, %Y" }}</time><div>{{ item.text | markdownify | remove: '<p>' | remove: '</p>' }}</div></li>
{% endfor %}
</ul>
{% else %}
<p>No news yet.</p>
{% endif %}
