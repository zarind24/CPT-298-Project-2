Project Proposal
1. Project Identification
Project Title: Load Maine Town Data to PostgreSQL Warehouse
Course: CPT-298
Term: Spring 2026
Student Name(s): Hayden Allen, Zarin Deane
Primary Contact: Zarin Deane
Proposed Start Date: 4-2-2026
Proposed End Date: 5-3-2026
2. Project Selection & Motivation
Describe why you selected this project and why you are a good fit.

Include:

Personal or professional motivation
Alignment with career goals
Relevant interests or prior exposure
--- For this project we both want to gain more experience in uploading data to a database. We also want to gain more experience in coding in Python in general. We see ourselves using Python or potentially loading things into a database in our future careers. We think this would look good as a project completed on our resumes. We have a bit of experience with this from our last project. We uploaded messages from our Discord bot into a database.

3. Problem Statement
Clearly describe the problem, need, or opportunity this project addresses.

Answer:

What problem exists?
Who is affected?
Why does this problem matter?
Limit to 1–2 focused paragraphs.

--- The problem is we need to upload Maine Town Data into the PostgreSQL Warehouse. This data is crucial for the CPT 166 SQL class as they will be using this data for their class. The data on the website is updated over time but without an automation updating it to the database the information for the CPT 166 class will be outdated.

4. Proposed Solution Overview
Provide a high-level description of your proposed solution.

Include:

What you intend to build, deploy, or configure
Core features or capabilities
Explicit exclusions (what the project will not include)
--- We plan to build a script using Python that downloads the data. Then it will organize it using data tables, and will then load it to the PostegreSQL warehouse. We will have the script run twice a year scanning for changes before each class starts their semester. The project will not include: A user interface, advanced analysis, and real time updates only scheduled.

5. Technical Stack & Tools
List the technologies you expect to use. Please note that this solution MUST live within the cpt.internal network and must be maintainable by future students.

Operating System(s): Linux Ubuntu
Programming Language(s): Python
Frameworks / Libraries: Pandas, Requests, psycopg2
Databases / Storage: PostegreSQL
Infrastructure (VMs, containers, etc.): Virtual Machine
Tools (Git, CI, monitoring, APIs, etc.): Git, Cron, ArcGIS dataset
6. Prerequisite Knowledge & Skills
Assess your readiness for this project.

Include:

Skills you already have
Skills you need to learn
Relevant coursework completed
Prior projects or experience
Be honest—this section helps scope the project appropriately.

--- We already have some experience with uploading basic data into a database. We don't have a full grasp on taking from a website and uploading into a database. We would be learning how to scan a website and pull information periodically to update the data. Relevant coursework has been: Discord bot uploading messages into a database, networking assignments, python assignments.

7. Project Scope & Deliverables
Define what success looks like.

Include:

Minimum viable deliverable (MVP)
Required outputs (application, scripts, documentation, etc.)
Optional stretch goals (if time permits)
--- Minimum (MVP): A script that downloads, cleans, loads the data, and a scheduled job that runs automatically

Deliverables:

Python script PostgreSQL table with data Documentation Basic error handling

Stretch goals: Only update changes that are big like a new town, Use PostGIS for location data, and better logging

8. Milestones & Timeline
Provide a rough timeline broken into phases.

Example:

Phase 1: Research & Design
Phase 2: Core Implementation
Phase 3: Testing & Refinement
Phase 4: Documentation & Presentation
Dates do not need to be exact, but planning is required.

Phase 1: Research & come up with a plan
Phase 2: Start working on code
Phase 3: finish code & troubleshoot
Phase 4: Create a presentation & fix any final problems
9. Risks, Constraints & Dependencies
Identify potential challenges.

Include:

Technical risks
Time constraints
External dependencies (APIs, credentials, access)
Mitigation strategies
--- There may be dataset form changes which could break the code or force updates to it which CPT students or the professor will need to go in and fix. We don't see there being an issue with time on this project. We should be able to complete the project within the time frame. We will need access to the CPT database. We plan to start simple and slowly get more technical to minimize risk of changes.

10. Security, Ethics & Safety Considerations
Address any relevant concerns, such as:

Authentication and authorization
Data sensitivity
Network exposure
Logging, monitoring, or automation impact
Ethical considerations
A brief assessment of all of these is required, even if it is "N/A".

--- This project involves minimal security and ethical concerns since the dataset being used is publicly available and does not contain sensitive information. However, proper security practices will still be followed. Access to the database will require authentication, and credentials will be stored securely and not exposed in scripts or logs. The system will run within the internal network, limiting external exposure. Logging will be implemented carefully to avoid including sensitive information.

11. Team Structure (If Applicable)
If working in a group, describe:

Team roles
Communication plan
Conflict resolution approach
Workload distribution
--- Zarin: Writes code to extract the data and organize it Hayden: Writes code to load into data base and scheduling We plan to use the new weekly meeting minutes to discuss over our project. We also will utilize Discord to communicate. We will split up work more evenly if we see an issue in someone doing too much work. We will also communicate issues early and not let them get worse.

12. Documentation & Knowledge Transfer Plan
Explain how this project will be documented. Please note that this should include documentation in the UVDesk knowledgebase at the very least. Programming projects should include readme.md files.

Include:

README or user documentation
Deployment or maintenance guides
How another student or administrator could continue the project
--- We will have a readme clearly explaining all steps of how to go about reading our project and what it does. We will have comments within our code that easily identify what each section of code does. We plan to keep our files organized as well with clearly labels on what each file is. We wont have the scheduling code in the same file and the extraction code. We want this to be an easy set up and well documented so students in the future can easily read and make updates to our project. Future improvements could include adding better error handling, supporting incremental updates instead of full reloads, or integrating geospatial features using tools like PostGIS. Because the system is modular, individual parts (data extraction, transformation, or loading) can be updated or replaced without rebuilding the entire project.

13. Faculty/cpt.internal Resources Requested
List any required resources:

VM access
Network access
Credentials or APIs
Special permissions
Hardware (if applicable)
Please be sure to consider any future tickets you may need to submit to complete this work as those will need to be generated and assigned to the appropriate groups as soon as feasibly possible once the project kicks off to ensure timely delivery. I will step in to help where required but you will likely be working with students in other classes so please be cognizant of their time!

Linux VM access PostgreSQL database access Permission to run cron jobs

Possible future requests:

Database setup help Network permissions

14. Acknowledgement of Expectations
By submitting this proposal, I acknowledge that:

This is a self-directed technical project
I am responsible for research and troubleshooting
Evaluation will consider process, documentation, and professionalism
Signature (Name & Date):

Student 1: Zarin Deane____________________ Date: 4-2-2026_______ Student 2: Hayden Allen____________________ Date: 4-2-2026_____ Student 3: ____________________________ Date: _______________ Student 4: ____________________________ Date: _______________

Instructor: ____________________________ Date: _______________
