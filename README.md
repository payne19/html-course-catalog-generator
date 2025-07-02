## html-course-catalog-generator
A Python script that sanitizes filenames and folder names in a course directory and generates a structured, searchable index.html file for browsing course content. The output is styled with dark mode support and includes a search bar powered by JavaScript and CSS.

Features
1. Sanitizes all file and folder names to remove problematic characters

2. Recursively walks through all subfolders

3. Includes files with extensions: .mp4, .pdf, .html, .url, .txt

4. Generates a nested HTML index reflecting the folder hierarchy

5. Adds icons based on file types for better readability

6. Dark mode toggle and search bar included (requires accompanying styles.css and script.js)

Usage
python generate_index.py "/path/to/your/course/folder"
This will:

  Sanitize names inside the specified folder
  Create a index.html file in the root of the directory

  Output
    index.html – Main file for browsing content

Uses:
  1. styles.css – For styling (dark mode, layout)
  2. script.js – For search functionality and theme toggle

Open index.html in any browser to explore the course contents.

## Notes
Subfolders prefixed with numbers (e.g., 01_Introduction) are sorted naturally

Icons are added for file types:

🎬 .mp4
📄 .pdf
🔗 .html, .htm
📃 .txt, .url
