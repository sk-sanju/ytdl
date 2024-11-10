<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Downloader Web App - README</title>
    <style>
        /* Basic Styling for the Readme page */
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }

        header {
            background-color: #333;
            color: #fff;
            padding: 1rem;
            text-align: center;
        }

        h1, h2, h3 {
            font-weight: bold;
        }

        .content {
            margin: 2rem;
        }

        .section {
            margin-bottom: 2rem;
        }

        code {
            background-color: #f0f0f0;
            padding: 0.2rem;
            font-family: monospace;
            border-radius: 4px;
        }

        .installation, .usage, .deployment, .license {
            background-color: #fff;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        pre {
            background-color: #f0f0f0;
            padding: 1rem;
            border-radius: 4px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body>

    <header>
        <h1>YouTube Downloader Web App - README</h1>
    </header>

    <div class="content">
        <section class="section features">
            <h2>Features</h2>
            <ul>
                <li>Download YouTube videos by simply providing the video URL.</li>
                <li>Supports video formats like MP4.</li>
                <li>User-friendly interface with a clean, modern design.</li>
                <li>Background image with a blurred effect to make the UI visually appealing.</li>
                <li>Fast download processing using yt-dlp.</li>
            </ul>
        </section>

        <section class="section technologies">
            <h2>Technologies Used</h2>
            <ul>
                <li><strong>Backend:</strong> Django (Python)</li>
                <li><strong>Video Downloading:</strong> yt-dlp library</li>
                <li><strong>Frontend:</strong> HTML5, CSS3</li>
                <li><strong>JavaScript:</strong> For dynamic behaviors (if needed)</li>
                <li><strong>Web Design:</strong> Custom CSS with a background blur effect</li>
                <li><strong>Deployment:</strong> Can be deployed on a cloud platform like Heroku, DigitalOcean, etc.</li>
            </ul>
        </section>

        <section class="section prerequisites">
            <h2>Prerequisites</h2>
            <p>Before you begin, ensure you have the following installed:</p>
            <ul>
                <li>Python 3.x</li>
                <li>Django (Installation details below)</li>
                <li>yt-dlp library</li>
            </ul>
        </section>

        <section class="section installation">
            <h2>Installation</h2>
            <p>Follow these steps to install and run the project locally:</p>
            <pre><code>git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader</code></pre>

            <p>Create and activate a virtual environment:</p>
            <pre><code># For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate</code></pre>

            <p>Install required dependencies:</p>
            <pre><code>pip install -r requirements.txt</code></pre>

            <p>If you don't have a <code>requirements.txt</code>, you can install dependencies manually:</p>
            <pre><code>pip install django yt-dlp</code></pre>

            <p>Set up your database:</p>
            <pre><code>python manage.py migrate</code></pre>

            <p>Add static files:</p>
            <pre><code># Ensure the static folder exists with the appropriate structure
your_project/
├── manage.py
├── your_project/
│   ├── settings.py
├── static/
│   ├── images/
│   │   └── logo.png
│   ├── css/
│   │   └── style.css
│   └── js/
└── templates/</code></pre>

            <p>Run the development server:</p>
            <pre><code>python manage.py runserver</code></pre>

            <p>After running this command, the app should be accessible at <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> in your browser.</p>
        </section>

        <section class="section usage">
            <h2>Usage</h2>
            <p>Open the web app in your browser (<a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>).</p>
            <p>Enter the YouTube video URL in the input field.</p>
            <p>Click the "Download" button to start downloading the video.</p>
            <p>The video will be downloaded and saved to your default download location.</p>
        </section>

        <section class="section deployment">
            <h2>Deployment</h2>
            <p>For deployment on cloud platforms like Heroku or DigitalOcean, follow their respective instructions on how to deploy a Django app.</p>
            <p><strong>For Heroku:</strong> Follow <a href="https://devcenter.heroku.com/articles/django-app-configuration" target="_blank">Heroku's Django Deployment Guide</a>.</p>
            <p><strong>For DigitalOcean:</strong> Follow <a href="https://www.digitalocean.com/community/tutorials" target="_blank">DigitalOcean's Django Deployment Guide</a>.</p>

            <h3>Static Files in Production</h3>
            <p>In production, run the following command to collect static files:</p>
            <pre><code>python manage.py collectstatic</code></pre>
            <p>This will gather all your static files (e.g., images, CSS, JS) into the <code>staticfiles</code> folder for proper deployment.</p>
        </section>

        <section class="section license">
            <h2>License</h2>
            <p>This project is licensed under the MIT License - see the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>
        </section>
    </div>

</body>
</html>
