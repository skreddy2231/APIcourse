# APIcourse

Setup Virtual Environments in Python:

	Allow us install different packages outside the installations of your local computer.
https://www.youtube.com/watch?v=IAvAlS0CuxI

**Step1**: below download and install virtualenv 
#pip install virtualenv
-- restart terminal and type <virtualenv> and see usage

**Step2** - create new project using virtualenv
#virtualenv myprojectA
Go to inside project and activate pip virtual project
#cd myprojectA
myprojectA# scripts\activate

myprojectA# where pip     --- check where pip all the time before and after virtualenv create. it tells pip path.

myprojectA# pip install numpy==1.22.0     
		or 
myprojectA# pip install numpy
myprojectA# scripts\deactivate.bat

-- check project specific packages and versions.
**Step3**: myprojectA# pip list

**Step4**: Create requirement.txt  file, that only packages available  related to my project 
a. myprojectA# pip freeze
b. myprojectA# pip freeze --local

this adds diff packages and can add in git repo as one project for team.
c. myprojectA# pip freeze --local  > requirements.txt
---------------------------------
	
