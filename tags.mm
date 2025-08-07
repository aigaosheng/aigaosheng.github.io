---
title: Tags
layout: default
description: Browse posts by tags
header-img: "image/rawa-sun-falling2-a.png"
permalink: "/tags/"
---

<!-- Page Header -->
<header class="intro-header" style="background-image: url('{{ site.baseurl }}/{% if page.header-img %}{{ page.header-img }}{% else %}{{ site.header-img }}{% endif %}')">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
        <div class="site-heading" id="tag-heading">
          <h1>{{ page.title }}</h1>
          <span class="subheading">{{ page.description }}</span>
        </div>
      </div>
    </div>
  </div>
</header>

<!-- Main Content -->
<div class="container">
  <div class="row">
    <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">

	<!-- tag -->
	<div id='tag_cloud_1' class="tags">
		{% for tag in site.tags %}
		<a href="#{{ tag[0] }}" title="{{ tag[0] }}" rel="{{ tag[1].size }}">{{ tag[0] }}</a>
		{% endfor %}
	</div>		

      <!-- Tag Cloud -->
      <section id="tag-cloud" class="tags mb-4">
        <h2>All Tags</h2>
        <div class="tag-cloud">
          {% for tag in site.tags %}
            <a href="#{{ tag[0] | slugify }}" class="tag-link" title="{{ tag[0] }} - {{ tag[1].size }} posts" rel="{{ tag[1].size }}">
              {{ tag[0] }} ({{ tag[1].size }})
            </a>
          {% endfor %}
        </div>
        <hr>
      </section>

      <!-- Tagged Posts -->
      {% for tag in site.tags %}
        <section class="tag-section">
          <h3 id="{{ tag[0] | slugify }}" class="tag-title">
            <i class="fa fa-tag"></i> {{ tag[0] }}
          </h3>
          {% for post in tag[1] %}
            <div class="post-preview">
              <a href="{{ post.url | relative_url }}">
                <h4 class="post-title">{{ post.title }}</h4>
                {% if post.subtitle %}
                  <h5 class="post-subtitle">{{ post.subtitle }}</h5>
                {% endif %}
              </a>
              <p class="post-meta">
                <i class="fa fa-calendar"></i> {{ post.date | date: "%Y-%m-%d" }}
              </p>
            </div>
            <hr>
          {% endfor %}
        </section>
      {% endfor %}

    </div>
  </div>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const hash = window.location.hash;
    if (hash) {
      const target = document.querySelector(hash);
      if (target) {
        target.scrollIntoView({ behavior: "smooth" });
      }
    }
  });
</script>
