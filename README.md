<picture>
  <source media="(max-width: 600px)" srcset="./assets/profile/header-mobile.png">
  <img src="./assets/profile/header.png" alt="Ayush Patel · Backend systems and databases · B.Tech at IIIT Bangalore" width="100%">
</picture>

I like working on the parts of software you only notice when they go wrong. In my systems projects, that means figuring out who can update a shared inventory file and how a database estimates the number of rows a query will match.

**I’m open to software engineering internships**, especially on teams working on backend services, infrastructure, or data systems. [Connect on LinkedIn ↗](https://www.linkedin.com/in/ayush-patel-72a037316/)

## ShopSync

**What happens when two customers try to buy the last item?** I built a multi-client store in C to explore that question. The server forks a worker for each TCP connection. Those workers share inventory on disk, so I used POSIX semaphores and advisory file locks to coordinate their writes.

<picture>
  <source media="(max-width: 600px)" srcset="./assets/profile/server-mobile.png">
  <img src="./assets/profile/server.png" alt="Two TCP clients connect to separate worker processes. Both workers access the same locked inventory file." width="100%">
</picture>

[See where the server forks a worker](https://github.com/Ayush-patel9/OS/blob/main/Server.c#L797-L811) · [Inspect the inventory lock](https://github.com/Ayush-patel9/OS/blob/main/Server.c#L67-L79) · [Run ShopSync locally](https://github.com/Ayush-patel9/OS#readme)

## Databases and search

### How much data does a histogram need?

I sampled **1,000, 3,000, and 5,000 rows** from a PostgreSQL table and used dynamic programming to choose histogram boundaries. The experiment compares the largest selectivity error for numeric IDs and text titles at each sample size. [See the results plot](https://github.com/Ayush-patel9/Histogram/blob/main/figures/sample_size%20vs%20max%20error.png) · [Read the experiment](https://github.com/Ayush-patel9/Histogram/blob/main/code/selectivity.py)

### ManakAI · Finding the right Indian standard

A procurement tender might name a standard by number or describe a product in ordinary language. ManakAI handles both with exact lookup and vector search, then follows links between standards in a reference graph. [Explore the retrieval code](https://github.com/Ayush-patel9/SIH_2026/blob/main/pipeline/rag_engine/tri_retrieval.py) · [See how results are ranked](https://github.com/Ayush-patel9/SIH_2026/blob/main/pipeline/rag_engine/reranker_fusion.py)

## Elsewhere in my work

- **Fletchly** lets a team ask questions about its internal documents through a React and TypeScript interface. [Open the demo](https://ayush-patel9.github.io/docubuddy-answer-central/) · [View source](https://github.com/Ayush-patel9/docubuddy-answer-central)
- **Umang 2025** is the campus festival website I contributed to at IIIT Bangalore. [Explore the site repository](https://github.com/Ayush-patel9/Umang2025)
- **Spring Boot e-commerce platform** is a team project where I worked with Java on a web application. [View the project](https://github.com/Ayush-patel9/JAVA_TEAM_COLDBLOODED)

<details>
  <summary>GitHub activity and more repositories</summary>

  <p><img src="./assets/profile/activity.svg" alt="My contribution calendar for the past year, refreshed weekly" width="100%"></p>
  <a href="https://github.com/Ayush-patel9?tab=repositories">Browse all repositories ↗</a>
</details>
