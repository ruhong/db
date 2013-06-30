---
title: css-rules
---


### 1. Protocol

```{.css}
/* Not recommended */
.example {
  background: url(http://www.google.com/images/example);
}

/* Recommended */
.example {
  background: url(//www.google.com/images/example);
}
```

### 2. Capitalization

```{.css}
/* Not recommended */
color: #E5E5E5;

/* Recommended */
color: #e5e5e5;
```

### 3. CSS Validity
> Use valid CSS where possible.
> [W3C CSS validator](http://jigsaw.w3.org/css-validator/)

### 4. ID and Class Naming
> Use meaningful or generic ID and class names.

```{.css}
/* Not recommended: meaningless */
#yee-1901 {}

/* Not recommended: presentational */
.button-green {}
.clear {}

/* Recommended: specific */
#gallery {}
#login {}
.video {}

/* Recommended: generic */
.aux {}
.alt {}
```

### 5. ID and Class Name Style
> Use ID and class names that are as short as possible but as long as necessary.

```{.css}
/* Not recommended */
#navigation {}
.atr {}

/* Recommended */
#nav {}
.author {}
```

### 6. Type Selectors
> Avoid qualifying ID and class names with type selectors.

```{.css}
/* Not recommended */
ul#example {}
div.error {}

/* Recommended */
#example {}
.error {}
```

### 7. Shorthand Properties
> Use shorthand properties where possible.

```{.css}
/* Not recommended */
border-top-style: none;
font-family: palatino, georgia, serif;
font-size: 100%;
line-height: 1.6;
padding-bottom: 2em;
padding-left: 1em;
padding-right: 1em;
padding-top: 0;

/* Recommended */
border-top: 0;
font: 100%/1.6 palatino, georgia, serif;
padding: 0 1em 2em;
```

### 8. Units and 0
> Omit unit specification after “0” values.

```{.css}
/* Recommended */
margin: 0;
padding: 0;
```

### 9. Leading 0s
> Omit leading “0”s in values.

```{.css}
/* Recommended */
font-size: .8em;
```

### 10. Hexadecimal Notation
> Use 3 character hexadecimal notation where possible.

```{.css}
/* Not recommended */
color: #eebbcc;

/* Recommended */
color: #ebc;
```

### 11. ID and Class Name Delimiters
> Separate words in ID and class names by a hyphen.

```{.css}
/* Not recommended: does not separate the words “demo” and “image” */
.demoimage {}

/* Not recommended: uses underscore instead of hyphen */
.error_status {}

/* Recommended */
#video-id {}
.ads-sample {}
```

### 12. Declaration Stops
> Use a semicolon after every declaration.

```{.css}
/* Not recommended */
.test {
  display: block;
  height: 100px
}
/* Recommended */
.test {
  display: block;
  height: 100px;
}
```

### 13. Property Name Stops
> Use a space after a property name’s colon.

```{.css}
/* Not recommended */
h3 {
  font-weight:bold;
}

/* Recommended */
h3 {
  font-weight: bold;
}
```

### 14. Declaration Block Separation
> Use a space between the last selector and the declaration block.

```{.css}
/* Not recommended: missing space */
#video{
  margin-top: 1em;
}

/* Not recommended: unnecessary line break */
#video
{
  margin-top: 1em;
}

/* Recommended */
#video {
  margin-top: 1em;
}
```

### 15. Selector and Declaration Separation
> Separate selectors and declarations by new lines.

```{.css}
/* Not recommended */
a:focus, a:active {
  position: relative; top: 1px;
}

/* Recommended */
h1,
h2,
h3 {
  font-weight: normal;
  line-height: 1.2;
}

### 16. Rule Separation
> Separate rules by new lines.

html {
  background: #fff;
}

body {
  margin: auto;
  width: 50%;
}
```

### 17. CSS Quotation Marks
> Use single quotation marks for attribute selectors and property values.

```{.css}
/* Not recommended */
@import url("//www.google.com/css/maia.css");

html {
  font-family: "open sans", arial, sans-serif;
}

/* Recommended */
@import url(//www.google.com/css/maia.css);

html {
  font-family: 'open sans', arial, sans-serif;
}
```
