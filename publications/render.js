(function () {
  var container = document.getElementById('publications-auto');
  if (!container) return;

  fetch('/publications/data.json')
    .then(function (res) {
      if (!res.ok) throw new Error('fetch failed');
      return res.json();
    })
    .then(function (data) {
      var pubs = data.publications || [];
      if (!pubs.length) throw new Error('empty');

      // Group by year, descending
      var byYear = {};
      pubs.forEach(function (p) {
        var y = p.year || 'n.d.';
        if (!byYear[y]) byYear[y] = [];
        byYear[y].push(p);
      });
      var years = Object.keys(byYear).sort(function (a, b) { return b - a; });

      var html = '';
      if (data.updated) {
        html += '<p class="pub-loading" style="font-size:0.78rem;margin-bottom:0;">Last synced with Google Scholar: ' + data.updated + '</p>';
      }
      years.forEach(function (year) {
        html += '<h2 class="pub-year">' + year + '</h2><ul class="pub-list">';
        byYear[year].forEach(function (p) {
          var titleTag = p.scholar_url
            ? '<a class="pub-title" href="' + esc(p.scholar_url) + '" target="_blank" rel="noopener noreferrer">' + esc(p.title) + '</a>'
            : '<span class="pub-title">' + esc(p.title) + '</span>';
          var badge = p.scholar_url
            ? '<a class="pub-badge" href="' + esc(p.scholar_url) + '" target="_blank" rel="noopener noreferrer">Scholar ↗</a>'
            : '';
          html += '<li class="pub-item">'
            + titleTag
            + '<span class="pub-authors">' + esc(p.authors) + '</span>'
            + '<span class="pub-meta"><span class="pub-journal">' + esc(p.journal || '') + '</span>' + badge + '</span>'
            + '</li>';
        });
        html += '</ul>';
      });
      container.innerHTML = html;
    })
    .catch(function () {
      container.innerHTML = '<p class="pub-fallback">Publications could not be loaded automatically. '
        + 'See the full list on <a href="https://scholar.google.com/citations?user=Fqnde5sAAAAJ" '
        + 'target="_blank" rel="noopener noreferrer">Google Scholar</a>.</p>';
    });

  function esc(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
})();
