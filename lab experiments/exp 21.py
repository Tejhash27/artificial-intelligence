
from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>My Educational Blog</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f2f2f2;
            margin: 0;
        }

        header {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }

        nav {
            background-color: #555;
            padding: 15px;
            text-align: center;
        }

        nav a {
            color: white;
            margin: 15px;
            text-decoration: none;
        }

        section {
            background: white;
            margin: 20px;
            padding: 20px;
            border-radius: 8px;
        }

        img {
            width: 300px;
        }

        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 15px;
        }
    </style>
</head>

<body>

<header>
    <h1>Welcome to My Educational Blog</h1>
    <p>Learning HTML and Web Development</p>
</header>

<nav>
    <a href="#home" title="Go to Home">Home</a>
    <a href="#about" title="About this Blog">About</a>
    <a href="#html" title="Learn HTML Tags">HTML Tags</a>
    <a href="#contact" title="Contact Us">Contact</a>
</nav>

<section id="home">
    <h2>Home</h2>
    <p>
        Welcome to my blog! This website demonstrates
        different HTML tags used in web development.
    </p>
</section>

<section id="about">
    <h2>About This Blog</h2>
    <p>
        This blog provides basic information about HTML,
        hyperlinks, images, headings and other HTML elements.
    </p>

    <img src="https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png"
         alt="HTML5 Logo" title="HTML5 Logo">
</section>

<section id="html">
    <h2>HTML Tags Demonstration</h2>

    <h3>1. Title Tag</h3>
    <p>The title tag displays the webpage title in the browser tab.</p>

    <h3>2. Anchor Tag</h3>
    <p>Anchor tags are used to create hyperlinks.</p>
    <a href="https://www.google.com"
       title="Visit Google">Click Here to Visit Google</a>

    <h3>3. Heading Tags</h3>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>

    <h3>4. Paragraph Tag</h3>
    <p>This is an example of a paragraph tag.</p>

    <h3>5. Image Tag</h3>
    <p>The image tag is used to display images on a webpage.</p>

    <h3>6. Bold and Italic Tags</h3>
    <p><b>This text is bold.</b></p>
    <p><i>This text is italic.</i></p>

    <h3>7. List Tags</h3>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>Python</li>
    </ul>
</section>

<section id="contact">
    <h2>Contact Us</h2>
    <p>Email: example@gmail.com</p>
    <a href="mailto:example@gmail.com"
       title="Send Email">Send an Email</a>
</section>

<footer>
    <p>Copyright 2026 My Educational Blog</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_code)


if __name__ == "__main__":
    app.run(debug=True)
