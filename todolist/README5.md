# Assignment 5 Essay

## What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?

#### Internal CSS

Internal or embedded CSS requires you to add `<style>` tag in the `<head>` section of your HTML document.

This CSS style is an effective method of styling a single page. However, using this style for multiple pages is time-consuming as you need to put CSS rules on every page of your website.

Advantages of Internal CSS: You can use class and ID selectors, Since you’ll only add the code within the same HTML file, you don’t need to upload multiple files.

Disadvantages of Internal CSS: Adding the code to the HTML document can increase the page’s size and loading time.

#### Inline CSS

Inline CSS is used to style a specific HTML element. For this CSS style, you’ll only need to add the style attribute to each HTML tag, without using selectors.

This CSS type is not really recommended, as each HTML tag needs to be styled individually. Managing your website may become too hard if you only use inline CSS.

However, inline CSS in HTML can be useful in some situations. For example, in cases where you don’t have access to CSS files or need to apply styles for a single element only.

#### External CSS
With external CSS, you’ll link your web pages to an external .css file, which can be created by any text editor in your device (e.g., Notepad++).

This CSS type is a more efficient method, especially for styling a large website. By editing one .css file, you can change your entire site at once.

## Describe the HTML5 tags that you know.
`<head>` = 	Specifies information about the document
`<body>` =  Specifies the body element
`<br>`   =  Inserts a single line break
`<button>` = Creating a Button
`<table>` = Creating a table
`<td>` = Table Cell

## Describe the types of CSS selectors you know.

Tag : Chooses an element based on it's tag.

```
p {
    insert code here
}
```

Class : Chooses an element based on given class name -->

```
.name-class {
    insert code here
}
```

Universal : Chooses all elements,

```
* {
    insert code here
}
```

## Explain how you would implement the checklist above.

1. Use bootstrap
2. Make cards for todolist.html and style todolist.html, login.html, register.html , create_task.html
3. Deploy to Heroku by pushing to GitHub