# To-Do-List Application

## Team Members
1. Suren A/L Krishnan (BAI_A2009F-2501003)
2. Ruhan A/L S.Gopi (202410063)
3. Emanuel Preston A/L Vincent (BIT_B2201F-2409001)
4. Priscilla A/P Sankar (BAI_B2009F-2409008)
5. Sambureni Lisa Ruramai (BDS_B2201F-2409002)

## 1.0 Introduction to the Application

This assignment is a To-Do-List Application developed for the **Software Engineering course (BAI21113), Assignment 1**. This is a Python based application designed  to help users effectively manage their daily tasks. 

## The app allows users to:  
1. Add new task
2. View all tasks
3. Delete task
4. Mark Task as completed 
5. View Done/Pending Tasks
6. Categorize task
7. Prioritize task 
8. Set due dates for each task

The main goal of this application is to improve personal productivity by providing a simple yet efficient task management system, which enables users to track their responsibilities  and stay organized. 

This assignment  involves three structured iterations each adding new functionality and a user friendly graphical interface (GUI). 

## 1.1 Technologies Used
### 1.1.0 Development Tools & Process 

**1.  Followed an iterative development process, manages through:**
Git & GitHub 
Used for version control, structured branching, adding commit messages, merging, tagging and project documentation through README.md file. Did collaborate with group members by creating an account for each. 


**In this assignment it contains 4 README.md files:** 
1. Main → Project overview (this file)
2. Iteration-1  
3. Iteration-2
4. Iteration-3 


**Kanban board (via GitHub Projects)** 
Used to visualize and manage tasks, ensuring clarity and steady progress throughout the project lifecycle.


**More details are provided below:**
Section 3.0: GitHub Usage
Section 4.0: Kanban Board 


**2. Programming Language Used**
Python used for all: 
* Main Logic application 
* Graphical User Interface → via Tkinter
* Persistent data handling → via JSON

## 2.0 Iterative Development Overview 
This To-Do-List Application using an iterative development approach. This project was divided into three major iterations, each iteration introducing new features. Importantly, builded upon the previous iteration by adding new features by increasing its complexity. 

Below is summary of the three iterations:

## 2.1 Iteration-1 
Build core features of To-Do-List Application. 

**Key features:**
1. Add new task
2. View all tasks
3. Delete task
4. Mark Task as completed 
5. View Done/Pending Tasks
	
**Focus**
* Clear functional base for task management 
* Simple, text-based user interface
* Implemented core task logic via CRUD operations


## 2.2 Iteration-2
Enhance task management by allowing new features to add in by building upon pervios iteration-1


**New features added:**
	1. Assign Categorization to task (e.g., Study, Personal, Work) 
	2. Set priority Level (High, Medium, Low) 
	3. Add due dates for each task. 

**Focus**
Improving task organization
Providing planning support 
Increase complexity of the application 

## 2.3 Iteration-3
Improve user experience with Graphical User interface (GUI) and persistent storage

**New features added:**
1. Full GUI developed using Tkinter
2. Store tasks on JSON files+8
3. GUI based input for category, priority and due date
4. Button and visual display of all core functions. 

**Focus**
* User friendly interface
* Visual clarity 
* Store data

## 2.4  Iteration Overall Explanation 
Each iterations detailed explanation, challenges faced, commit messages added explained under the respective README.md iteration branches, ***(refer to tags)***

1. Iteration-1 → Core Functions
2. Iteration-2 → New features
3. Iteration-3 → GUI and data persistence


## 3.0 Github Usage 
This section explains how Git and Github were used effective version control for this assignment by ensuring a structured and traceable development process. 

### 3.1 Initial Repository Set up 
Created a new public repository and was named appropriately as per selected application for assignment which is “ToDoList_App”  in short and memorable way. 


**The following step was taken:**
1. Created Repository under this link https://github.com/
2. Named repository as “ToDoList_App”
3. Choose Public repository 
4. Initialized Repository with: 
	* Added README.md file 
	* Added .gitignore with chosen programming language of python
5. Created Repository 

This picture shows repository overview showing README.md and .gitignore in initial commit: ############################

## 3.2 Git Workflow 
### 3.2.1 Branching Strategy
In order to ensure organized and manageable development, a clear branching strategy was used throughout this assignment. Branching is an important part of version control. Specifically, one branch for each development iteration was created. 

**Branches Created** 
Iteration-1 → Core task Management (CRUD) 
Iteration-2 → advanced features
Iteration-3 → GUI and persistent storage 

Each development process was accomplished under each branch.The main branch remained stable and received the branches via merging strategy after completing and testing. 

**Steps taken to create branches:** 
1. After initializing a repository set up on Github, for each development process, branches were created. 
2. After creating branches, each branch will have its own README.md and .gitignore file. 
3. Afterwards, for each iteration branch an empty python code file .py was uploaded by clicking “upload files button”

 **For example for iteration-1 branch:**
In initial stage each branches will have: 
* Iteration-1 (README.md, .gitignore, Iteration_1.py)
* Iteration-2 (README.md, .gitignore, Iteration_2.py)
* Iteration-3 (README.md, .gitignore, Iteration_3.py)

4. In the empty python file under each iteration, code has been written, by a clear and descriptive commit message. Refer to section 3.2.2 for more explanation.  

**Why Was This Decision Made to Use branches?**
* To isolate development for each iteration and avoid confusion or overwriting
* To allow better focus and organization by keeping unrelated changes in separate branches
* To match the structure required in the assignment guidelines for version control

**How This Helped Manage the Assignment**
* Made it easier to manage changes step-by-step without mixing features
* Allowed for clean, logical commit histories in each branch
* Helped with tracking progress clearly and simplified version review during submission


## 3.2.2 Commit Workflow
In this assignment, a clean and consistent commit history was accomplished to ensure  clarity, traceability and version control. For each iteration branch, a structured commit strategy was followed. 


**Steps taken for Commit Workflow:** 
1. As mentioned in 3.2.1 (step 3), an empty Python file was uploaded under each iteration using GitHub’s “Upload file” feature. 
2. Each section of the code was first written and tested in Visual Studio Code to ensure correctness and eliminate any bugs before uploading into GitHub. Testing strategy was applied here. Refer to section 3.2.3 Testing Strategy 
3. After testing each functional part ,that specific code block was copy-pasted into the corresponding Python file in GitHub
A meaningful commit message with description was added for each section to describe the purpose of the update.
4. For example, for iteration-1 (First Commit) 
a) Firstly, as for iteration 1, the first code was written in visual studio code where it displayed the main menu, initialized the task list and handled user input through a loop with a basic validation (no features yet). 
b) This tested code was pasted into iteration1.py under iteration-1 branch. 
c) A commit message with description was added.
d) And saved the changes
5. Step 2-4 were repeated for each functional block of code (e.g. add to task, delete task) until the final tested version of the iteration code was completed. 

This commit workflow was consistently followed for all three iterations until it was fully completed. 


### 3.2.3 Clear and Consistent Commit message
A clear and consistent commit message format was followed using prefixes: 
* Feat: → Added new features 
* Fix: → Fixed bugs or error

### 3.2.3 Testing Strategy
All functionalities were manually tested for each iteration before the code was committed to GitHub. This approach ensured that only bug-free and stable code was uploaded.

All testing was performed locally using Visual Studio Code, before code uploaded into Github. 

**Testing Workflow**
1. As mentioned in, section 3.2.2 commit workflow (step 2), “Each section of the code was first written and tested in Visual Studio Code to ensure correctness and remove any bugs before uploading.“ . Here manually each feature testing was accomplished. 

For example, 
a. Is the menu printed out correctly ? 
b. Can tasks be added ? 
c. Can tasks be deleted ? 
d. Does the GUI respond to button clicks and update the task accordingly ? 
e. Are the tasks saved ? 


2. If any bugs occur during testing, they were resolved immediately before the code was committed into GitHub. In order to ensure GitHub uploaded code is free of bugs and stable. 

**This method, does helps with Git Commits** 
1. Only working code was pushed 
2. Created a clean Git history 


## 3.2.4 Tagging Strategy

To clearly mark completion of each development phase, Git tags were used for each iteration. 

**Tag Format:**
1) v1.0 → Iteration 1 completed 
2) v2.0 → Iteration 2 completed
3) v3.0 → Iteration 3 completed

**Workflow:**  
As mentioned, all work is done through the GitHub web interface. After the final code block was copy pasted into the GitHub iteration .py  file under each branch. Tag has been created. 

1. Clicked on the releases tab, and create a new release button was clicked under tags box.
2. Under choose tag, added tag name, while target was which branch need to be tagged. 
	**For example,**
	Under choose tag, v1.0 target was iteration-1, respectively same goes for other branches.
3. Add in release title, with description and clicked “publish release button”
4. Tag was created.

***Remark***: *Tagging was completed before merging. This is because tags are flexible, they can be deleted or recreated anytime. However, for merging strategy, once it is merged into main, it becomes part of main history, and it cannot be unmerged easily as tags. Therefore, tagging was done prior to merge.* 

**The main purpose of tagging,** 

**1. Version Separation** 
* Each tag like v1.0 v2.0 v3.0 represents a specific completed stage of completion. 
* Helps to separate and identify different version of application 
* If anyone wants to look through assignment 1 , iteration 1 core function, they can click tag v1.0 and view files from iteration 1 only which is (README.md, .gitginore, iteration1.py) 

**2.Testing reference** 
* A tag marks a stable point in code which shows that it has been tested and confirmed to work. 
* If bugs occurs in future version, it can be easily undo the tag unlike merging. 

**3. Release management**  
* The manager can view the final version in clearer form under tags. 
* It counts as a deliverable final state of the project.

## 3.2.5 Merging
Merging was an essential part of this assignment to consolidate completed iteration work into the main branch in a clean and structured way. Since all code developed and tested were completed branch wise, merging was only done once each iteration was finalized and tagged. 

**Merging Workflow** 
1. After tagging, clicked on “pull request” tab
2. Clicked ‘New pull request”
* Base: main 
* Compare iteration-1 or depends on which branch to be merged. 
3. Added title and description
4. Clicked merge pull request and finally “Confirm merge”
5. After merging successfully, under mian the merged file will be there. 

**Maintaining Main README After Merge**
After merging an iteration branch into main, GitHub automatically updates all files — including the README.md — based on the merged branch.This means the iteration's README may overwrite the main branch README.


**Steps Taken**
1. After each merge, checked the main README.
2. If it was replaced,  manually copied and restored the original main content using GitHub’s Edit button.

**Why This Decision Was Made:**
* Tagging before merging helped lock in a version snapshot for future reference 
* Merging only after full checks ensured only stable and tested code reached main
* Manual README verification maintained clean documentation throughout all stages


**How Merging Helped this Assignment ?** 
* Easy to combine all features built in a dedicated iteration branch into the main project. 
* Ensures each version merged is completed, tested and tagged before being art of the final application
* Keeps the main branch clean and only contains stable code from completed iterations. 

## 3.3 Github Challenges
During the version control process using Github, a few challenges were encountered and addressed as follows:
1. Preserving README.MD During Merging
* **Challenge:** When merging iteration branches into main, the README.md file from the iteration branch sometimes replaced the original main README content.
* **Solution:** After each merge,manually checked and restored the correct README.md content in the main branch by copy-pasting the intended version. 

2. Tagging Timing
* **Challenge:** GitHub allows tags to be deleted, but merges are permanent. It was important to make sure everything was finalized before tagging and merging.
* **Solution:** I only applied tags like v1.0, v2.0, and v3.0 after rechecking all code, README files, and commit history to ensure correctness before merging.

3. Sequential Uploads with Commit 
* **Challenge:** Uploading and committing code section by section through the web interface required careful version control to avoid mixing features.
* **Solution:** I followed a consistent strategy of copy-pasting code feature-by-feature, committing with clear messages (feat:, fix:, etc.) to maintain a logical commit history.


## 4.0 Kanban Board
* ***Kanban Board Screenshots***: *Screenshots of your Kanban board at three different stages can be refer to Kanban folders for the pictures.* 

Did used GitHub Projects to create a Kanban board after completing the main development phases. The board had columns for Backlog, To Do, In Progress, Testing, and Done.Instead of planning tasks ahead, we mostly used the board to organize and track completed tasks from each iteration. This helped us confirm that all features were implemented correctly.

**Challenges:**
* We often forgot to update the board during development, so it wasn’t helpful for real-time tracking.
* Most tasks were added after coding was done, so the board didn’t support collaboration or planning during the process.

**Benefits:**
* It was still useful for reviewing our progress at the end. By organizing tasks into columns, we could clearly see:
* Which features were completed
* Whether the iteration goals were met
* If any features were missing

Overall, the Kanban board helped us double-check our work and get a clear overview of the entire project.



