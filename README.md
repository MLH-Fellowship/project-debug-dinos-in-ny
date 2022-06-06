## Inspiration
This project was inspired by the countless impressive online portfolios we've seen created by other developers. As we embark on our journey as MLH Fellows, it's only fitting that we have our own platforms to update and improve as we gain new skills and experiences.

## What it does
The website starts at a landing page which contains a navigation bar that directs the user to our portfolios. From there, the user is able to select dropdown menus that contain information about us and links to our GitHub accounts.

The pages that contain information about us include photos of us, photos of our hobbies, and details about our education and work experience. The pages also include interactive Google Maps features that allow the user to view live footage from global locations we have visited.

## How we built it
To start, we designed our landing page using HTML and CSS. Next, we crafted our webpages with HTML and CSS as well. While our portfolios have the same HTML foundation, we used CSS to convey our individuality and interests.

There were five core parts to each portfolio:

1) An ‘about yourself section’ with a photo included.

2) Previous work experience.

3) Current/previous education.

4) Hobbies with images included.

5) A map of all the locations/countries each person visited.

Part 1 was achieved with HTML and CSS. Parts 2, 3, 4 and 5 required some back-end development. Using Flask, a micro web framework written in Python, and Jinja, a Python web template engine, we were able to connect a backend database of our work experience, hobbies and education. We wrote data within the Python file, passed that data to the front end and finally rendered the final product with the designated information.

Specific pieces of data we rendered in using Jinja are:
- Our names

- School information (university, major)

- Our hobbies

For part 5 of our portfolios, we used Google Data Studio to visualize our travel data with a Google Maps feature.

## Challenges we ran into
**Sristi**: One notable challenge that I had to overcome was figuring out how to use Git/GitHub, and Flask. I had to read documentation and watch numerous tutorials to try and get everything working, from library installations, to making sure that my VSCode was properly syncing the changes that I was making.

**Aima**: The biggest challenge I ran into was handling static and moving features on the webpages with CSS. It was jarring to have elements fly off the page when I would make changes to other elements. One thing that was really helpful was looking at other webpages I thought were really well structures and using the 'Inspect' option on Google Chrome to see how they formatted their code.

## Accomplishments that we're proud of
**Sristi**: I’m proud of learning a vast amount of new information in a short amount of time. The skills that I gained from this project are definitely ones that I am going to keep having to use throughout my tech career, so being able to learn about them and successfully utilize what I learned offered a gratifying feeling.

**Aima**: I'm proud of having learned new things while honing skills I already have. I'm also proud of Sristi and I for working well together in such a short amount of time. We were able to divide and conquer and help each other through obstacles.

## What we learned
**Sristi**: Learned how to use Flask, manuever through GitHub and Git basics.

**Aima**: I learned about how versatile Python can be. I also learned how to navigate GitHub a lot better.

## What's next for Debug Dinos in NY
Over the course of this fellowship, we hope to bolster our portfolios and migrate them to individual websites. We also hope to personalize our pages more with CSS and see what more data we can incorporate with Jinja.
