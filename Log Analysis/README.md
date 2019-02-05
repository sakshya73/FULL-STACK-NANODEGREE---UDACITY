**************************** LOG ANALYSIS PROJECT ****************************

Aim of the Program :
    1. To find out the most popular 3 articles.
    2. To find out which authors get the most page views on their articles.
    3. Days on which there were more than 1% requests that led to errors.

Requirements:
    1. Download vagrant.
        You can download it from vagrantup.com .
    2. Download VirtualBox.
        You can download it from virtualbox.org.
    3. Download VM Configuration.
        You can fork and clone it from
        https://github.com/udacity/fullstack-nanodegree-vm . 
        
How to run the Program :
    1. Download database(zip) on which operations are to be performed.
    2. Extract the file in vagrant directory.
    3. Download the project.
    4. Extract all files in vagrant directory.
    5. Open terminal in your system.
    6. Change the path to vagrant.
    7. Use "vagrant up" command to setup Virtual Machine.
    8. Use "vagrant ssh" to login.
    9. Change path to /vagrant/Project.
   10. Run psql -d NEWS -f newsdata.sql for loading the data.
   11. Now simply run the command "python project3.py".
  
Sample Output :
     MOST POPULAR ARTICLES
1 . Candidate is jerk, alleges rival  =  338647 views
2 . Bears love berries, alleges bear  =  253801 views
3 . Bad things gone, say good people  =  170098 views

 MOST POPULAR AUTHORS
1 . Ursula La Multa  =  507594 views
2 . Rudolf von Treppenwitz  =  423457 views
3 . Anonymous Contributor  =  170098 views

DATE WITH MORE THAN 1 % ERROR:
July 17, 2016 had 2 % errors.
