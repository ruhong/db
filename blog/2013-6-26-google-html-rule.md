---
title: html-rules
---


### 1. Protocol

```{.html}
<!--Not recommended-->
<script src="http://www.google.com/js/gweb/analytics/autotrack.js"></script>

<!-- Recommended -->
<script src="//www.google.com/js/gweb/analytics/autotrack.js"></script>
```

### 2. Capitalization
> All code has to be lowercase: This applies to HTML element names, attributes,      attribute values (unless text/CDATA), CSS selectors, properties, and property values (with the exception of strings).

```{.html}
<!-- Not recommended -->
<A HREF="/">Home</A>

<!-- Recommended -->
<img src="google.png" alt="Google">
```

### 3. Encoding
> Use UTF-8 (no BOM).

```{.html}
<meta charset="utf-8">
```

### 4. Comments
> Explain code as needed, where possible.

```{.html}
<!-- Explain something -->
```

### 5. Document Type
> Use HTML5.

```{.html}
<!DOCTYPE html>
```

### 6. HTML Validity
> Use valid HTML where possible.
> [W3C HTML validator](http://validator.w3.org/nu/)

### 7. Semantics
> Use HTML according to its purpose.

```{.html}
<!-- Not recommended -->
<div onclick="goToRecommendations();">All recommendations</div>

<!-- Recommended -->
<a href="recommendations/">All recommendations</a>
```

### 8. Multimedia Fallback
> Provide alternative contents for multimedia.

```{.html}
<!-- Not recommended -->
<img src="spreadsheet.png">

<!-- Recommended -->
<img src="spreadsheet.png" alt="Spreadsheet screenshot.">
```

### 9. Optional Tags
> Omit optional tags (optional).

```{.html}
<!-- Not recommended -->
<!DOCTYPE html>
<html>
  <head>
    <title>Spending money, spending bytes</title>
  </head>
  <body>
    <p>Sic.</p>
  </body>
</html>

<!-- Recommended -->
<!DOCTYPE html>
<title>Saving money, saving bytes</title>
<p>Qed.
```

### 10. type Attributes
> Omit type attributes for style sheets and scripts.

```{.html}
<!-- Not recommended -->
<link rel="stylesheet" href="//www.google.com/css/maia.css" type="text/css">

<!-- Recommended -->
<link rel="stylesheet" href="//www.google.com/css/maia.css">

<!-- Not recommended -->
<script src="//www.google.com/js/gweb/analytics/autotrack.js" type="text/javascript"></script>

<!-- Recommended -->
<script src="//www.google.com/js/gweb/analytics/autotrack.js"></script>
```

### 11. General Formatting
> Use a new line for every block, list, or table element, and indent every such child element.

```{.html}
<blockquote>
  <p><em>Space</em>, the final frontier.</p>
</blockquote>

<ul>
  <li>Moe
  <li>Larry
  <li>Curly
</ul>

<table>
  <thead>
    <tr>
      <th scope="col">Income
      <th scope="col">Taxes
  <tbody>
    <tr>
      <td>$ 5.00
      <td>$ 4.50
</table>
```

### 12. HTML Quotation Marks
> When quoting attributes values, use double quotation marks.

```{.html}
<!-- Not recommended -->
<a class='maia-button maia-button-secondary'>Sign in</a>

<!-- Recommended -->
<a class="maia-button maia-button-secondary">Sign in</a>
```

