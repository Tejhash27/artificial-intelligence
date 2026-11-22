# Create a Web Blog using Python

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>My Technology Blog</title>
</head>

<body style="font-family: Arial; margin: 40px;">

    <h1>Welcome to My Technology Blog</h1>

    <h2>About Technology</h2>

    <p>
        Technology makes our life easier.
        It helps us communicate, learn and work.
    </p>

    <h2>Latest Technology</h2>

    <img src="https://placehold.co/400x200"
         alt="Technology Image"
         width="400">

    <p>
        Technology is growing every day.
        <b>Artificial Intelligence</b> is an
        important development.
    </p>

    <h2>Useful Websites</h2>

    <a href="https://www.google.com"
       title="Visit Google">
       Click Here to Visit Google
    </a>

    <br><br>

    <a href="https://wordpress.com"
       title="Visit WordPress">
       Create Your Own Blog
    </a>

    <h2>More Information</h2>

    <p><i>Thank you for visiting my blog!</i></p>

    <hr>

    <p>Copyright 2026 - My Technology Blog</p>

</body>
</html>
"""

# Save HTML file
with open("myblog.html", "w", encoding="utf-8") as file:
    file.write(html_code)

print("Web Blog created successfully!")
print("Open myblog.html in your browser.")
