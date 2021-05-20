# Django Personal Portfolio

My personal portfolio website built in Django. A dynamic website for an engineer/scientist/programmer. 

I developed this project as a way to improve my web-development skills (including learning more about Django) and to finally build a personal website for myself. While this could have been done (almost) all statically, I wanted to play a little with Django, so I implemented some dynamic functionalities.

This project contains the following apps:
* Blog
* Publications
* Projects
* Main

## Dynamic behaviour

While the site is static for unauthorised users (it always serves the same content), it contains an admin page where content can be added, eddited and/or removed. This makes it easier to update the website without having to deploy new files.


## Blog

The blog app has a markdown textfield ([markdownx](https://github.com/neutronX/django-markdownx)), a banner for the detail view, a thumbnail for the list view, and a tag field handled by [django-taguluous](https://radiac.net/projects/django-tagulous/). The author of the posts is connected via a foreign-key relationship.

## Publications

The publications app handles a list of publications (articles, books, conference papers, etc.) for the website's author. For each publication, the owner can input the publication's authors (as a string), it's publication date, publisher and type. It also links to an information about the owner and highlights the owner's contributions, i.e. a list of authors "A Owner, J Doe" would be highlighted as "**A Owner**, J Doe" if the owner's initials were set as "A Owner".

## Projects

The projects app is very similar to the blog app. It also has a markdown textfield ([markdownx](https://github.com/neutronX/django-markdownx)), a banner for the detail view, a thumbnail for the list view, and tow tag fields handled by [django-taguluous](https://radiac.net/projects/django-tagulous/). The user can click on each project and read more about it.

## Main app

The main app handles the main information about the website's owner. It contains models for education, experiences, expertises and info. Within the info, the owner can update their profile pic, personal statement (brief description), initials and email without having to deploy new code to the server. The info model is a simpleton.

**While the code for this website is open source, its content (including images, assets, journal posts, projects) is copyrighted and should not be reproduced.**




