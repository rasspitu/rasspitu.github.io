---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of all the pages on this site. There is also an [XML version]({{ base_path }}/sitemap.xml) for search engines.

<h2>Pages</h2>
{% for post in site.pages %}
  {% if post.title and post.sitemap != false %}{% include archive-single.html %}{% endif %}
{% endfor %}

{% if site.publications.size > 0 %}
<h2>Publications</h2>
{% for post in site.publications %}
  {% unless post.sitemap == false %}{% include archive-single.html %}{% endunless %}
{% endfor %}
{% endif %}
