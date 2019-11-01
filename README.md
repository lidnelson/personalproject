# Character Sheet Generator
This craetes a character sheet generator for people to utilise of getting to know the character and how they would speak, or act. So far it covers personality what they look like and the sort of things that get on thier nerves. there are more things that can be added that ill make the application much better. These are yet to be added

## The Requirements to Run
In the folder **personalproject/character_sheets** there is a file called *requirements.txt*.

        sudo apt-get update
        sudo apt-get install python3-pip

        pip3 install -r requirements.txt

## Running the Application
There are three different ways run this application with helpof files in the **personalproject/character_sheets** repository 


### Local 
In a virtual box 
1. Change directory into structure in the terminal
    
        . /venv/bin/activate
    
2. Change diectory to character sheet

        export FLASK_APP=run.py
        export FLASK_ENV=development
        flask run

#### Using a virtual box
    
3. Navigate to http://localhost:5000/

#### Using google cloud platform 

3. Navigate to http://{{ External IP address }}:5000/  
    
*Remember when creating the VM in gcp to tick both the HTTP and HTTPS traffic*

### SystemD
1. Run the systemd.sh script 
2. Navigate to http://{{ External IP address }}:5000/  
    
### Docker
In the respisitory **personalproject/character_sheet** 
1. build the docker image naming it whatever you like
2. use command line 

        docker run -d -p {{ No.:No. }} --name {{name of the container}} {{name of the image}} .

3. Navigate to http://{{ External IP address }}:{{No.}}/  
## Building the App
