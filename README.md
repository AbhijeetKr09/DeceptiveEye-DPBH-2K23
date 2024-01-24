# Deceptive Eye - Dark pattern buster Hackthon

Deceptive Eye is a Chrome extension that detects and highlights dark patterns on e-commerce websites. It reads text on `product` pages of shopping websites, then identifies and classifies dark pattern text. These potential dark patterns are then highlighted, with a popup that identifies and explains the category that a given dark pattern belongs to. 

With the reference of the research paper *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites* (Mathur et al.) and their dataset of dark pattern strings we have trained our classifier,  with the help of page segmentation algorithm, we broke down webpages into meaningful blocks of text.

## Tech Stack
The Chrome Extension front-end that scrapes the active web page is written in Javascript. For the back-end, a Python server running Flask interfaces Bernoulli Naive Bayes models to classify tokens of text sent to it. To train these algorithms, datasets from Princeton University researchers along with manually annotated datasets were used.
## Installation
`pip install requirement.txt`

Install the Chrome extension:
1. Navigate to chrome://extensions
2. Enable "Developer mode" by toggling the switch at the top right of the page
3. Click the "Load unpacked" button.
4. Navigate to the repository directory, and select the folder `app` for installation
5. Ensure that the extension is enabled.
the extension has been successfully installed!
## Reference
Research Paper
Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M., & Narayanan, A. (2019). Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. Proceedings of the ACM on Human-Computer Interaction, 3(CSCW), 81.

TEAM NAME
Abhijeet Kumar
Manhvi Yadav
Iqbal Ansari
Harshita Sharma
Shivam Agarwal

